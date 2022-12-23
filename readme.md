
# RKCU - Royal Kludge Color Utility
Python3 based command line utility to manage LED color profiles on [Royal Kludge RK 61 Keyboard](https://www.meckeys.com/shop/keyboard/60-keyboard/royal-kludge-rk61-hot-swappable/).

## Dependencies

    hidapi
Installable using pip by running :

    $ pip install hidapi

## How to use:

    # python rkcu.py <arguments>

Arguments :

    --speed, --sp [1-5]
    # speed of led animation.
    
    --brightness, -br [0-5]
    # brightness of led animation
	
	--sleep, -sl [1-5]
	# sleep duration for the keyboard led
	 - 1: 05 Minutes
	 - 2: 10 Minutes
	 - 3: 20 Minutes
	 - 4: 30 Minutes
	 - 5: Never Sleep
	
	--rainbow, -rb
	# Set LED color mode to Rainbow
	
	--red, -r 0-255
	# Red value of Color
	
	--green, -g 0-255
	# Green value of Color
	
	--blue, -b 0-255
	# Blue value of Color
	
	--animation, -an "animation_name"
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
	 - neon
	 - shadow_disappear
	 - flash_away

Example :

    # python rkcu.py --speed 3 --brightness 5 --sleep 5 -r 255 -g 255 -b 255 -an "ripples_shining"
    # python rkcu.py -sp 5 -an "rotating_storm" -rb

## Notes
- The `--rainbow` argument will overrule the `--red, --green, --blue` parameters.

- By default the script would require superuser access to run. In order to run this without root, you can plug a udev rule by performing the following steps :
Step 1: Find your vendor id and product id. Here it is `258a` and `004a` respectively, and would most likely be same for you if you are having the same keyboard.

    $ lsusb
    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 001 Device 005: ID 0c45:671e Microdia Integrated_Webcam_HD
    Bus 001 Device 002: ID 258a:004a SINO WEALTH RK Bluetooth Keyboard
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

	Step 2:
add a `rules` file to `/etc/udev/rules.d`
file: `60-rk.rules`

		SUBSYSTEMS=="usb|hidraw", ATTRS{idVendor}=="258a", ATTRS{idProduct}=="004a", TAG+="uaccess"

	replace `258a` with your vendor id and `004a` with your product id, in case it is different.

	Step 3:
	Finally, reload your udev rules by running the following command :

	    # udevadm control --reload-rules && udevadm trigger