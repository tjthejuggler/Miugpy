Miug allows the user to send midi signals or keypresses based on what they do with juggling balls.

Required software:
	Music software that can be controlled with midi or keypresses (VirtualDJ)
	https://www.virtualdj.com/download/
	Loopbe1 (midi only) http://www.nerds.de/en/loopbe1.html 

Setup:

	Keypress: In the preferences of your music software, associate a keypresses to the actions you wish to you, for instance Q:pause, and P:play. Then, in Miug use the following format to indicate which event type you want associated to which key: EventType,-KEY (examples: Gather,-Q or Ungather,-P). Note, only Gather and Ungather are currently usable with keypresses.
  
	MIDI: First install the free Loopbe1 software and make sure it is running. Next, open both Miug and whatever music software you are using. In the preferences of your music software find the 'controllers' or 'midi' section and select Loopbe. Now you must make a mapping between a midi signal and an action in your music software. In order to do this, go to the bottom right corner of Miug, and select a number from the first dropdown, the one with 'NOTE' above it. This should both add the currently selected midi note to the main textfield in Miug, and also send a midi signal through loopbe to your music software. This note should now be selectable in your music software, and you can map it to any action you like. Now when using the camera from Miug, that juggling event will be associated with that music action.


Event types:
	Gather - occurs when all visible balls are close enough together
	Ungather - occurs when balls are no longer gathered
	Location - uses the average location of all balls and translates it into a midi CC(slider).
		Works both vertically(locationv) and horizontally(locationh)
	Speed - uses the longest distance between any 2 visible balls and converts it into a midi CC(slider), the effect this has is that bigger, slower, juggling can be used to slow down music and smaller, faster juggling can be used to speed it up.
	Peak - if a ball is seen above a certain point then its horizontal location is transalted into a midi note.


Notes:
	-The current tracking system relies on glowing juggling balls and a dark room, the code looks for the largest white objects it sees and assigns a tracker to the 3 largest. The avereage of these trackers positions averaged over time is shown as well.
	-The syntax in the main textfield must be exactly right or it might crash.

Any questions or help setting it up or anything: tjthejuggler@gmail.com
