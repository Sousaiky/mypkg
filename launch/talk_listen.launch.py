<<<<<<< HEAD
#!/user/bin/python3
=======
#SPDX-FileCopyrightText: 2023 Soshi Saiki
#SPDX-Licence-Identifire: BSD-3-Clause
>>>>>>> ef89fdbf88fdb635bed7a5484a5fe3ac359f89c0

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions
import time

def generate_launch_description():

    talker = launch_ros.actions.Node(
        package='mypkg',
        executable='talker',
        )
    listener = launch_ros.actions.Node(
         package='mypkg',
         executable='listener',
         output='screen'
         )

    return launch.LaunchDescription([talker, listener])
