%{
clear all
%From IMReq
TargetY = 1640; %pixels
TargetX = 940; %pixels
TimeOfPic = 74843.3373;
%}
function TargetGPSCoords = FindTargetGPSCoords(TargetY, TargetX, TimeOfPic, California)

TargetPixels = [TargetY, TargetX];


%% Data Parsing

%C:\Users\Mateus Pinheiro\Documents\GitHub\AUVSI2018ImageProcessing
readfile1 = fileread( 'C:\Users\Mateus Pinheiro\Documents\GitHub\AUVSI2018ImageProcessing\TLM_Example2.txt' );
parsefile = strsplit(readfile1,",");
reshapefile = reshape(parsefile, 4, (length(parsefile))/4);
filetomatrix = str2double(reshapefile);

TimeData  = filetomatrix(1,:);
LatitudeData = filetomatrix(2,:);
LongitudeData = filetomatrix(3,:);
HeadingData = filetomatrix(4,:);

exit = 0;
i = floor(length(TimeData)/2);
j = length(TimeData);

while exit == 0
    
    if TimeOfPic == TimeData(i)
       HeadingInterp = HeadingData(i);
       GPSLATInterp = LatitudeData(i);
       GPSLONInterp = LongitudeData(i);
       
       exit = 1;
       
    elseif TimeOfPic > TimeData(i) && TimeOfPic < TimeData(i+1)
        Heading1 = HeadingData(i);
        Heading2 = HeadingData(i+1);
        PlaneGPSLAT1 = LatitudeData(i);
        PlaneGPSLAT2 = LatitudeData(i+1);
        PlaneGPSLON1 = LongitudeData(i);
        PlaneGPSLON2 = LongitudeData(i+1);
        TimeOfTelem1 = TimeData(i);
        TimeOfTelem2 = TimeData(i+1);
        
        HeadingInterp = InterpolationFunction(TimeOfPic,TimeOfTelem1, TimeOfTelem2, Heading1, Heading2);
        GPSLATInterp = InterpolationFunction(TimeOfPic,TimeOfTelem1, TimeOfTelem2, PlaneGPSLAT1, PlaneGPSLAT2);
        GPSLONInterp = InterpolationFunction(TimeOfPic,TimeOfTelem1, TimeOfTelem2, PlaneGPSLON1, PlaneGPSLON2);
        
        exit = 1;
        
    elseif TimeOfPic < TimeData(i) && TimeOfPic < TimeData(i-1)
        j = i;
        i = floor(i/2);
    else
        
        i = floor((i+j)/2);
        
    end
    
end



%% Interpolation

%{
TimeOfPic = 100;
TimeOfTelem1 = 99;
TimeOfTelem2 = 101;
Heading1 = 89;
Heading2 = 91;
PlaneGPSLAT1 = 33.933928;
PlaneGPSLAT2 = 33.933930;
PlaneGPSLON1 = -117.629775;
PlaneGPSLON2 = -117.629777;

HeadingInterp = InterpolationFunction(TimeOfPic,TimeOfTelem1, TimeOfTelem2, Heading1, Heading2);
GPSLATInterp = InterpolationFunction(TimeOfPic,TimeOfTelem1, TimeOfTelem2, PlaneGPSLAT1, PlaneGPSLAT2);
GPSLONInterp = InterpolationFunction(TimeOfPic,TimeOfTelem1, TimeOfTelem2, PlaneGPSLON1, PlaneGPSLON2);
%}

PlaneGPSInterp = [GPSLATInterp, GPSLONInterp];


%% Function Call
TargetGPSCoords = GPSLocalizationFunction(TargetPixels, HeadingInterp, PlaneGPSInterp, California)
end

function TargetLoc = GPSLocalizationFunction(TargetPixelLoc, Heading, GPSCoords, California)
    Resolution = [1640, 940]; %size of image
    FOV = [10.5626, 6.10052]; %deg
    TargetPixels = TargetPixelLoc; %where target is on image
    PlanePixels = [Resolution(1)/2, Resolution(2)/2]; %where plane is on image

    
    PixelVector = TargetPixels - PlanePixels; %distance from plane to target in pixels
    PercentVector = PixelVector./(Resolution/2); %distance from plane to target as a percentage of image size
    GroundSize = 70.*tand(FOV); %size of ground covered by field of view
    
    TargetLocPCoords = GroundSize .* PercentVector; %distance from plane to target in meters in the plane's coordinate system
    
    %TargetLocWCoords[1] = TargetLocPCoords[1]*cosd(Heading)+TargetLocPCoords[2]*sind(Heading); %East
    %TargetLocWCoords[2] = -TargetLocPCoords[1]*sind(Heading)+TargetLocPCoords[2]*cosd(Heading); %North
    
    TargetLocWCoords = [TargetLocPCoords(1)*cosd(Heading)+TargetLocPCoords(2)*sind(Heading), -TargetLocPCoords(1)*sind(Heading)+TargetLocPCoords(2)*cosd(Heading)];
    
    GPSChange = LatLonxy(TargetLocWCoords(1), TargetLocWCoords(2), California);
    
    TargetLoc = GPSCoords + GPSChange;
    
end




function GPSChange = LatLonxy(dX, dY, California)
if(California == 0) %We are in Maryland, Since 0 means false and 1 means true
     % Change in degrees Latitude for every meter {meter/deg}
     ChngX = 1.112684551E5;
     %1/ChngLon =8.987273079E-6                                                         SIMILAR TO ABOVE .....  .07% diff 
     % Change in degrees Longitude for every meter {meter/deg}
     ChngY = 8.750104301E4;
     % 1/ChngLon = 1.14284352E-5    aboveChngLon = 0.0000114353 .                       SIMILAR TO ABOVE.......  0.06% diff
     
     % Displacement of payload {meters}
     GPSChange = [dX*ChngX, dY*ChngY];
else %We are in California
     % Change in degrees Latitude for every meter {meter/deg}
     ChngX = 1.111785102E5;
     %1/ChngLon = 8.994543983E-6     aboveChngLat = 0.0000089931;                     SIMILAR TO ABOVE.............. 0.02% diff                    
                
     % Change in degrees Longitude for every meter {meter/deg}
     ChngY = 9.226910619E4; 
     %%1/ChngLon = 1.08378637E-5    aboveChngLon = 0.000010967;                        SIMILAR TO ABOVE........ 1.18%diff                                        
     
     % Displacement of payload {meters}
     GPSChange = [dX/ChngX, dY/ChngY];
end
end

function IterpParam = InterpolationFunction(PictureTime, TelemTime1, Telemtime2, Param1, Param2)

IterpParam = Param1 + (PictureTime - TelemTime1) * (Param2 - Param1)/(Telemtime2 - TelemTime1);

end
