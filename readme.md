# RKCU - Royal Kludge Color Utility
Python based command line utility to manage led color profiles on Royal Kludge RK 61 Keyboard.

How to use:

    python rkcu.py <arguments>

Arguments :

    --speed [1-5]
    # speed of led animation.
    
    --brightness [0-5]
    # brightness of led animation
	
	--sleep [1-5]
	# 1: 05 Minutes
	# 2: 10 Minutes
	# 3: 20 Minutes
	# 4: 30 Minutes
	# 5: Never Sleep
	
	--rainbow
	# Set LED color mode to Rainbow
	
	--red 0-255
	# Red value of Color
	
	--green 0-255
	# Green value of Color
	
	--blue 0-255
	# Blue value of Color
	
	--animation "animation_name"
	# List of availaible animations:
	 - neon_stream
	 - ripples_shining
	 - sine_wave
	 - rainbow_routlette
	 - stars_twinkle
	 - layer_upon_layer
	 - rich_and_honored
	 - marquee_effect
	 - rotating_storm
	 - serpentine_horse
	 - retro_snake
	 - diagonal_transformer
	 - ambilight
     	 - streamer
     	 - steady
	 - breathing
	 - neon": Animation.NEON,
     	 - shadow_disappear
	 - flash_away
