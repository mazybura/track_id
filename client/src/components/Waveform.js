import React, { useRef, useEffect, useState } from 'react';
import WaveSurfer from 'wavesurfer.js';
import './Waveform.css';

function Waveform({ fileUrl }) {
    const waveformRef = useRef(null);
    const waveSurferRef = useRef(null);
    const [isPlaying, setIsPlaying] = useState(false);
    const isMounted = useRef(true);

    useEffect(() => {
        isMounted.current = true;

        // Initialize WaveSurfer once
        if (waveformRef.current && !waveSurferRef.current) {
            waveSurferRef.current = WaveSurfer.create({
                container: waveformRef.current,
                waveColor: '#ddd',
                progressColor: '#E9DDB5',
                barWidth: 3,
                cursorColor: '#E9DDB5',
                responsive: true,
                height: 80,
            });

            waveSurferRef.current.on('finish', () => {
                if (isMounted.current) setIsPlaying(false);
            });
        }

        // Load new audio file when fileUrl changes
        if (fileUrl && waveSurferRef.current) {
            waveSurferRef.current.load(fileUrl);
        }

        return () => {
            isMounted.current = false;
            if (waveSurferRef.current) {
                waveSurferRef.current.destroy();
                waveSurferRef.current = null;
            }
        };
    }, [fileUrl]);

    const handlePlayPause = () => {
        if (waveSurferRef.current) {
            waveSurferRef.current.playPause();
            setIsPlaying(!isPlaying);
        }
    };

    return (
        <div className="waveform-wrapper">
            {fileUrl && (
                <>
                    <button className="play-pause-button" onClick={handlePlayPause}>
                        {isPlaying ? (
                            <i className="fas fa-pause"></i>
                        ) : (
                            <i className="fas fa-play"></i>
                        )}
                    </button>
                    <div className="waveform-container" ref={waveformRef}></div>
                </>
            )}
        </div>
    );
}

export default Waveform;
