import React from 'react';
import {AbsoluteFill, Composition, interpolate, registerRoot, useCurrentFrame} from 'remotion';
const Smoke=()=>{
  const frame=useCurrentFrame();
  const width=interpolate(frame,[0,45],[0,800],{extrapolateRight:'clamp'});
  return <AbsoluteFill style={{background:'#101b30',color:'#fff',justifyContent:'center',alignItems:'center',fontFamily:'sans-serif'}}>
    <h1 style={{fontSize:70,margin:15}}>VIDEO KIT</h1>
    <p dir="rtl" style={{fontSize:42}}>עריכה • תנועה • סיפור</p>
    <div style={{height:14,width:800,background:'#23314a',borderRadius:7,overflow:'hidden'}}>
      <div style={{height:14,width,background:'#66e7bc'}}/>
    </div>
  </AbsoluteFill>;
};
registerRoot(()=> <Composition id="KitSmoke" component={Smoke} width={1080} height={1080} fps={30} durationInFrames={60}/>);
