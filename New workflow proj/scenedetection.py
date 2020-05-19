import os
from scenedetect.video_manager import VideoManager
from scenedetect.scene_manager import SceneManager
from scenedetect.stats_manager import StatsManager
from scenedetect.detectors.content_detector import ContentDetector
from scenedetect.detectors.threshold_detector import ThresholdDetector



def find_scenes(video_path):

    video_manager = VideoManager([video_path])
    stats_manager = StatsManager()

    scene_manager = SceneManager(stats_manager)

 
    scene_manager.add_detector(ThresholdDetector())
    base_timecode = video_manager.get_base_timecode()

    scene_list = []

    try:
      
        if os.path.exists(stats_file_path):

            with open(stats_file_path, 'r') as stats_file:
                stats_manager.load_from_csv(stats_file, base_timecode)

  
        video_manager.set_downscale_factor()


        video_manager.start()

 
        scene_manager.detect_scenes(frame_source=video_manager)

 
        scene_list = scene_manager.get_scene_list(base_timecode)


   
        if stats_manager.is_save_required():
            with open(stats_file_path, 'w') as stats_file:
                stats_manager.save_to_csv(stats_file, base_timecode)

    finally:
        video_manager.release()

    return scene_list

print(find_scenes('./data/mi6.mp4'))