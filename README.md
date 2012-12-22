##FAQ
#What is Ikezawa?
Ikezawa is the developmental repository for the Katawa Shoujo pre-alpha port for the RenPSP Visual Novel Engine. Named after Hanako Ikezawa (because the port's quality is half-baked, wahaha~), this derivative project strives to deliver a full-fledged Ren'Py game into the primitive platform of the RenPSP.
#Why not use other Visual Novels?
In my observation, KS is one of the most known among the English visual novels. Aside from that, one of the few reasons why I started porting for the RenPSP is to bring Katawa Shoujo into the smaller screens. Luckily, another PSP user (or several of them, I forgot) who found out about the 0.2 release of the RenPSP wanted to play the same game.
#What's the difference between this and the real thing?
First of all, it would be the licensing infringement. Did a really huge no-no by stealing the brainchild of the Four Leaf Studios developers and making it into a craft of my own. You -- as the probable end-user -- and me will be fully responsible if this thing goes huge. Good luck to the two of us!

Second, the graphics have been modified into the size acceptable by the Lua Player used in the RenPSP platform. Unlike in Ren'Py, no image must exceed the size of 480 px in width and 272 px in height.

Third, no animations. Rendering for the Lua Player takes a lot of oomph for the PSP alone. Aside from that, transitions between acts will be static. The "currently stable" version of RenPSP (0.2) on Lua Player Euphoria v8 doesn't support video. Although we can trust RenPSP 0.3's Lua Player Plus for rendering video, a bug in its ability to read files suggest that we cannot run KS in it at all.

Fourth, no sound effects. Music files alone cause a lot of bloat in the Lua Player. If the RenPSP devs are lucky to set a wrapper for unloading sound files, then we just uncomment the script lines containing the SFX and watch the magic to happen.

Fifth, data exposure. That means, you can alter ANYTHING to the Ikezawa code or media and redistribute it as your own. There are two ways to prevent that: One is using a password-protected ZIP file to encase the content; Two is to wait hard until RenPSP has support for opening RPA files. Both of them are not stellar ideas.

#How do I place this in my PSP?
+ Download
+ Extract folder to ms0:/PSP/GAME/[RenPSP folder]/games
+ Execute

##DISCLAIMER
RenPSP is an independent release of lolbot from the iichan Eroge Team. RenPSP is NOT affiliated with iichan Eroge unless further specified. weetabix is not affiliated in either iichan Eroge Team, Four Leaf Studios, or the cereal Weetabix. The Ikezawa repository is not affiliated with GitHub's other Ikezawas. Katawa Shoujo is a release of Four Leaf Studios. Katawa Shoujo, its media, and its scripts are protected by Creative Commons license BY-NC-ND, which this repository is a direct violation of. Use all present data in this repository at your own risk.

For comments and suggestions regarding this repository or its contents, contact weetabix via e-mail [vovo27_miranemiko@yahoo.co.jp], Jabber [weetabix@jabber.org], Twitter [@weetabix_su], or GitHub [@weetabix-su].

You can also contact the repository's official Twitter account [@Wtbx_Ikezawa] and e-mail [kraftwerk.ikezawa@gmail.com].