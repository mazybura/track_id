import React, { useState } from 'react';
import axios from 'axios';
import Waveform from './Waveform';
import './DownloadForm.css';

function DownloadForm() {
    const [trackName, setTrackName] = useState('');
    const [message, setMessage] = useState('');
    const [fileUrl, setFileUrl] = useState(null);
    const [isLoading, setIsLoading] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setIsLoading(true);
        setMessage('');
        setFileUrl(null);

        try {
            const response = await axios.post('http://localhost:8000/download', {
                track: trackName
            });

            if (response.data.status === 'success') {
                // setMessage(`Successfully downloaded: ${trackName}`);
                setFileUrl(response.data.file_url);
            } else {
                setMessage('Error downloading the song');
            }
        } catch (error) {
            setMessage('An error occurred while downloading');
            console.error('Error:', error);
        } finally {
            setIsLoading(false);
        }
    };


    return (
        <div>
            <div className="form-container">
                { }
                <form onSubmit={handleSubmit}>
                    <label>
                        Song:
                        <input
                            type="text"
                            value={trackName}
                            onChange={(e) => setTrackName(e.target.value)}
                            placeholder="e.g., Headhunterz - Dragonborn"
                            required
                        />
                    </label>
                    <button type="submit" disabled={isLoading}> { }
                        {isLoading ? 'Downloading...' : 'Download'}
                    </button>
                </form>

                { }
                <div className="image-container">
                    <img src="\images\jump_logo.png" alt="Jumping Image" />
                </div>
            </div>

            {message && <p>{message}</p>}

            { }
            {isLoading && (
                <div className="loader"></div>
            )}

            { }
            {fileUrl && (
                <div className="waveform-wrapper"> { }
                    {fileUrl && <Waveform fileUrl={fileUrl} />}
                </div>
            )}
        </div>
    );
}

export default DownloadForm;
