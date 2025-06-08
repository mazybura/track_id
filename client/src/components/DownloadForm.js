import React, { useState } from 'react';
import axios from 'axios';
import Waveform from './Waveform';  // Import komponentu Waveform
import './DownloadForm.css'; // Import stylów

function DownloadForm() {
    const [trackName, setTrackName] = useState('');
    const [message, setMessage] = useState('');
    const [fileUrl, setFileUrl] = useState(null);
    const [isLoading, setIsLoading] = useState(false);  // Stan dla animacji ładowania

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
                setMessage(`Successfully downloaded: ${trackName}`);
                setFileUrl(response.data.file_url); // Ustawiamy fileUrl → wtedy Waveform odpali!
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
                {/* Formularz po lewej stronie */}
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
                    <button type="submit" disabled={isLoading}> {/* Wyłączanie przycisku podczas ładowania */}
                        {isLoading ? 'Downloading...' : 'Download'}
                    </button>
                </form>

                {/* Obraz po prawej stronie */}
                <div className="image-container">
                    <img src="\images\jump.png" alt="Jumping Image" />
                </div>
            </div>

            {message && <p>{message}</p>}

            {/* Animacja ładowania */}
            {isLoading && (
                <div className="loader"></div>
            )}

            {/* Użycie komponentu Waveform poza formularzem */}
            {fileUrl && (
                <div className="waveform-wrapper"> {/* Nowy wrapper dla Waveform */}
                    {fileUrl && <Waveform fileUrl={fileUrl} />}
                </div>
            )}
        </div>
    );
}

export default DownloadForm;
