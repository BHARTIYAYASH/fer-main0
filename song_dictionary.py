# song_dictionary.py
# Canonical weather keys (from Ambee docs)
AMBEE_WEATHER_KEYS = [
    "clear",
    "partly-cloudy",
    "cloudy",
    "rain",
    "snow",
    "fog",
]

# Helpful external-to-Ambee mapping (common external groups -> Ambee key)
# e.g. OpenWeatherMap groups: 2xx thunderstorm, 3xx drizzle, 5xx rain, 6xx snow, 7xx atmosphere (mist/haze), 800 clear, 80x clouds
WEATHER_CODE_MAP = {
    "2xx": "thunderstorm",      # map to inferred key
    "3xx": "rain",              # drizzle -> rain (use precip intensity for drizzle)
    "5xx": "rain",
    "6xx": "snow",
    "7xx": "fog",               # mist/haze -> fog (or inferred haze)
    "800": "clear",
    "80x": "partly-cloudy",     # choose partly-cloudy vs cloudy by cloud_cover threshold
}

# Main song dictionary:
# Structure: SONG_DICTIONARY[emotion][weather_key] = {
#     "genre": ...,
#     "acoustic_strategy": ...,
#     "tracks": [...],
#     "mechanism": ...
# }
SONG_DICTIONARY = {
    "neutral": {
        "clear": {
            "genre": "Chill Phonk / Instrumental Synthwave",
            "acoustic_strategy": "Repetitive 808 sub-bass, mid-tempo synth lines, instrumental (no vocals)",
            "tracks": ["Sahara - Hensonn", "Close Eyes - DVRST"],
            "mechanism": "Maintains cognitive focus and elevates baseline arousal without vocal distraction."
        },
        "partly-cloudy": {
            "genre": "Chill Phonk / Lo-fi instrumental",
            "acoustic_strategy": "Sustained low-mid synth pads with subtle rhythmic elements",
            "tracks": ["Sahara - Hensonn", "Close Eyes - DVRST"],
            "mechanism": "Keeps attention steady while remaining unobtrusive."
        },
        "cloudy": {
            "genre": "Bollywood Lofi (Slowed + Reverb)",
            "acoustic_strategy": "Heavy reverb + slowed tempo to create acoustic space",
            "tracks": ["Dil Ka Rishta (Lofi)", "Piya O Re Piya (Lofi)"],
            "mechanism": "Reverberation expansion creates psychological acoustic space matching overcast visuals."
        },
        "rain": {
            "genre": "Marathi Soft Acoustic / Nostalgic Hindi",
            "acoustic_strategy": "Mid-range acoustic frequencies; soft vocals",
            "tracks": ["Sunya Sunya - Timepass 2", "Boondon Se Baaten"],
            "mechanism": "Mid-range frequencies blend with precipitation noise to soothe the listener."
        },
        "fog": {
            "genre": "Ambient Chill / Cinematic Lo-Fi",
            "acoustic_strategy": "Ethereal pads, low-pass filtering, sparse percussive elements",
            "tracks": ["Valhalla - NERONUS", "Endless Night - SLEEP SPIRIT"],
            "mechanism": "Pads + low-pass mimic atmospheric density and reduce high-frequency stimulation."
        },
        "snow": {
            "genre": "Ambient / Minimal Instrumental",
            "acoustic_strategy": "Soft bells, slow pads, minimal beat",
            "tracks": ["Valhalla - NERONUS"],
            "mechanism": "Sparse textures support calmness in low-temperature, low-arousal states."
        },
        "thunderstorm": {
            "genre": "Ambient Chill / Low-impact Score",
            "acoustic_strategy": "Deep pads, gentle low-frequency rumble, soft predictable chord cycles",
            "tracks": ["Endless Night - SLEEP SPIRIT"],
            "mechanism": "Predictable textures reduce startle and support grounding during noisy weather."
        },
        "any": {
            "genre": "Instrumental Lo-fi",
            "acoustic_strategy": "Neutral, low-energy instrumental",
            "tracks": ["Sahara - Hensonn"],
            "mechanism": "Baseline focus support across conditions."
        }
    },

    "happiness": {
        "clear": {
            "genre": "South Indian Kuthu / Bollywood Dance",
            "acoustic_strategy": "High BPM, major-key, heavy syncopated percussion",
            "tracks": ["Arabic Kuthu - Anirudh", "Besharam Rang - Pathaan"],
            "mechanism": "Maximizes dopaminergic output and stimulates motor cortex (movement/joy)."
        },
        "partly-cloudy": {
            "genre": "Bollywood Pop / Feel-Good Anthems",
            "acoustic_strategy": "Brass sections, group chorus, mid-to-high energy",
            "tracks": ["Tune Maari Entriyaan", "Luv Ju - Bunty Aur Babli 2"],
            "mechanism": "Brass + chorus lift social joy and counter gray visuals."
        },
        "cloudy": {
            "genre": "Bollywood Pop / Anthems",
            "acoustic_strategy": "Uplifting chord progressions, brass, chorus",
            "tracks": ["Tune Maari Entriyaan", "Luv Ju - Bunty Aur Babli 2"],
            "mechanism": "Elevates social joy against overcast conditions."
        },
        "rain": {
            "genre": "Marathi Monsoon Joy / Romantic Hindi",
            "acoustic_strategy": "Sweeping strings + traditional percussion",
            "tracks": ["Mala Ved Lagle - Timepass", "Ek Ladki Bheegi Bhaagi Si"],
            "mechanism": "Culturally-conditioned romantic joy amplified by monsoon cues."
        },
        "fog": {
            "genre": "Hollywood Instrumental Pop / Tropical",
            "acoustic_strategy": "Bright xylophone-like tones, major harmonies",
            "tracks": ["Toucans - Tatono"],
            "mechanism": "Pure tonal content fools the brain into tropical warmth, countering dullness."
        },
        "any": {
            "genre": "Upbeat Instrumental Pop",
            "acoustic_strategy": "Positive major-key hooks, danceable groove",
            "tracks": ["Toucans - Tatono"],
            "mechanism": "Directly boosts mood regardless of weather."
        }
    },

    "surprise": {
        "clear": {
            "genre": "Aggressive Phonk / Hardstyle",
            "acoustic_strategy": "Heavy sidechain, sudden 808 drops, extreme frequency shifts",
            "tracks": ["Neon Blade - MoonDeity", "Murder Plot - Kordhell"],
            "mechanism": "Converts shock into energised arousal without long-term anxiety."
        },
        "partly-cloudy": {
            "genre": "High-Energy Bollywood Reveal",
            "acoustic_strategy": "Unpredictable synth drops, sudden vocal entrances",
            "tracks": ["Aavan Jaavan - War 2", "Dhating Naach"],
            "mechanism": "Keeps auditory cortex in anticipatory arousal for novelty."
        },
        "cloudy": {
            "genre": "Aggressive Electronic / Cinematic",
            "acoustic_strategy": "Large dynamic swings, sudden percussive stabs",
            "tracks": ["Neon Blade - MoonDeity"],
            "mechanism": "Maintains high neurological engagement, transforms surprise into action."
        },
        "rain": {
            "genre": "Cinematic Trailer Music / Epic Score",
            "acoustic_strategy": "Staccato strings, sudden silences, explosive brass",
            "tracks": ["Air Raid - Chroma", "Furious Retribution"],
            "mechanism": "Mimics environmental unpredictability, channels startle into excitement."
        },
        "fog": {
            "genre": "Cinematic / Ambient Surprise",
            "acoustic_strategy": "Sparse ambiences punctuated by sudden transient events",
            "tracks": ["Air Raid - Chroma"],
            "mechanism": "Triggers curiosity while preventing panic."
        },
        "any": {
            "genre": "Unexpected Genre-Bending Covers",
            "acoustic_strategy": "Familiar lyric set in shocking instrumentation",
            "tracks": ["The Sound of Silence - Disturbed"],
            "mechanism": "High novelty keeps attention focused on music rather than unpleasant surprise."
        }
    },

    "sadness": {
        "clear": {
            "genre": "South Indian / Malayalam Soft Indie",
            "acoustic_strategy": "Acoustic guitars, breathy vocal performances",
            "tracks": ["Cherathukal", "Arerey Manasa"],
            "mechanism": "Empathic comfort without demanding high physiological energy."
        },
        "partly-cloudy": {
            "genre": "Soft Indie / Lyrical Empathy",
            "acoustic_strategy": "Warm acoustic timbres, close-mic vocals",
            "tracks": ["Everybody Hurts - R.E.M.", "True Love Waits - Radiohead"],
            "mechanism": "Lyrical empathy promotes self-soothing and reduces isolation."
        },
        "cloudy": {
            "genre": "English Self-Compassion / Empathy",
            "acoustic_strategy": "Slow tempi, intimate vocal lines",
            "tracks": ["Everybody Hurts - R.E.M.", "True Love Waits - Radiohead"],
            "mechanism": "Directly addresses cognitive sorrow and aids processing."
        },
        "rain": {
            "genre": "Marathi Sad / Nostalgic Folk",
            "acoustic_strategy": "Sweeping strings, traditional instrumentation",
            "tracks": ["Olya Sanjveli - Premachi Goshta", "Sunya Sunya"],
            "mechanism": "Culturally resonant container for grief processing."
        },
        "fog": {
            "genre": "Bollywood Soulful / Slow Ballads",
            "acoustic_strategy": "Minor keys, extended vocal legato",
            "tracks": ["Rait Zara Si", "Ek Dil Ek Jaan"],
            "mechanism": "Facilitates catharsis in low-visibility / introspective environments."
        },
        "any": {
            "genre": "Low-energy Acoustic",
            "acoustic_strategy": "Minimal arrangement, empathetic lyricism",
            "tracks": ["True Love Waits - Radiohead"],
            "mechanism": "Low demand listening encourages emotional processing."
        }
    },

    "anger": {
        "clear": {
            "genre": "Aggressive Phonk / Drift Phonk",
            "acoustic_strategy": "Distortion, heavy 808 clipping, high BPMs",
            "tracks": ["Fatality - Kordhell", "Vendetta! - MUPP"],
            "mechanism": "Matches sympathetic arousal and allows safe discharge via music."
        },
        "partly-cloudy": {
            "genre": "Bollywood Revenge / Motivational",
            "acoustic_strategy": "Anthemic builds, heavy percussion",
            "tracks": ["Aarambh Hai Prachand", "Dangal - Title Song"],
            "mechanism": "Redirects anger into focused motivation and physical energy."
        },
        "cloudy": {
            "genre": "Bollywood Motivational / Anthemic",
            "acoustic_strategy": "Strong rhythms, marching percussion",
            "tracks": ["Dangal - Title Song"],
            "mechanism": "Transforms diffuse anger into task-oriented vigor."
        },
        "rain": {
            "genre": "Indian Classical (Cooling) / Raga",
            "acoustic_strategy": "Soothing microtonal phrases, slow tempo",
            "tracks": ["Saraswathi Raag Compositions"],
            "mechanism": "Microtones interact with auditory cortex to lower cortisol and muscle tension."
        },
        "thunderstorm": {
            "genre": "Cinematic Dark / Epic Orchestral",
            "acoustic_strategy": "Massive orchestral hits, heavy low brass",
            "tracks": ["Furious Retribution - Epic Score"],
            "mechanism": "Grand externalisation of frustration in a controlled way."
        },
        "any": {
            "genre": "Controlled High-energy / Motivational",
            "acoustic_strategy": "Power rhythms with regulated tempo",
            "tracks": ["Fatality - Kordhell"],
            "mechanism": "Channel sympathetic arousal into productive action."
        }
    },

    "fear": {
        "clear": {
            "genre": "Bollywood Slow / Gentle Romance",
            "acoustic_strategy": "Slow BPM (60-70), predictable chord progressions",
            "tracks": ["Dil Jaaniye", "Hoor"],
            "mechanism": "Heart-rate entrainment and predictable chords signal safety to amygdala."
        },
        "partly-cloudy": {
            "genre": "English Acoustic / Soft Self-Care",
            "acoustic_strategy": "Warm acoustic guitars and empathetic lyrics",
            "tracks": ["Light On - Maggie Rogers", "Fear is a Liar - Zach Williams"],
            "mechanism": "Reduces cognitive spirals and grounds the listener."
        },
        "cloudy": {
            "genre": "Acoustic Self-care",
            "acoustic_strategy": "Low dynamics, reassuring lyrical content",
            "tracks": ["Light On - Maggie Rogers"],
            "mechanism": "Encourages cognitive grounding through familiarity."
        },
        "rain": {
            "genre": "Healing Frequencies / Solfeggio",
            "acoustic_strategy": "Drone frequencies (396Hz/432Hz) and slow textures",
            "tracks": ["396Hz Energy Cleanse", "432Hz Indian Classical"],
            "mechanism": "Continuous drone inhibits threat-detection and lowers physiological arousal."
        },
        "fog": {
            "genre": "Ambient Instrumental / Nature Sounds",
            "acoustic_strategy": "No sudden percussive transients; gentle field recordings",
            "tracks": ["Blissful and Calm", "A Day Without Rain"],
            "mechanism": "Prevents startle reflex and fosters safe slow breathing."
        },
        "any": {
            "genre": "Soft Acoustic / Healing Frequencies",
            "acoustic_strategy": "Slow predictable progressions",
            "tracks": ["Dil Jaaniye"],
            "mechanism": "Heart-rate entrainment and reassurance."
        }
    },

    "disgust": {
        "clear": {
            "genre": "South Indian Pop / Upbeat Dance",
            "acoustic_strategy": "High-fidelity production, bright leads",
            "tracks": ["Rowdy Baby", "Enjoy Enjaami"],
            "mechanism": "Overrides aversive cognitive loops with high sensory engagement."
        },
        "partly-cloudy": {
            "genre": "Instrumental Pop / Pure Tones",
            "acoustic_strategy": "Consonant xylophone-like instruments, clean mixes",
            "tracks": ["Toucans - Tatono", "Misery Business - Paramore"],
            "mechanism": "Acts as acoustic palate-cleansing, resetting aesthetic centers."
        },
        "cloudy": {
            "genre": "Instrumental Pop / Bright Production",
            "acoustic_strategy": "Clear mixes, bright synths, upbeat rhythm",
            "tracks": ["Toucans - Tatono"],
            "mechanism": "Forces positive sensory re-evaluation."
        },
        "rain": {
            "genre": "Marathi Clean Melodies / Acoustic",
            "acoustic_strategy": "Crystal-clear vocal engineering and consonant string harmonies",
            "tracks": ["Tu Havishi - Online Binline", "Qayde Se"],
            "mechanism": "Elicits purity feelings that match cleansing visuals of rain."
        },
        "fog": {
            "genre": "Bright Instrumental / Palate Cleanser",
            "acoustic_strategy": "High clarity pure tones",
            "tracks": ["Toucans - Tatono"],
            "mechanism": "Resets sensory disgust loops."
        },
        "any": {
            "genre": "High-fidelity Upbeat Pop",
            "acoustic_strategy": "Clean mixes, saturated high frequencies, major keys",
            "tracks": ["Enjoy Enjaami"],
            "mechanism": "Overrides aversive states with high sensory reward."
        }
    },

    "contempt": {
        "clear": {
            "genre": "R&B / Self-Care Pop",
            "acoustic_strategy": "Warm basslines, affirming lyrics",
            "tracks": ["Put Your Records On", "Self Care - Louis the Child"],
            "mechanism": "Dissolves harsh self-criticism and promotes acceptance."
        },
        "partly-cloudy": {
            "genre": "Conscious Hip-Hop / Empathetic Pop",
            "acoustic_strategy": "Narrative lyrics, warm instrumentation",
            "tracks": ["Keep Ya Head Up - Tupac", "1-800-273-8255 - Logic"],
            "mechanism": "Storytelling reduces distance and builds shared humanity."
        },
        "cloudy": {
            "genre": "Conscious Hip-Hop / Empathy",
            "acoustic_strategy": "Story-driven lyrics with warm backings",
            "tracks": ["Keep Ya Head Up - Tupac"],
            "mechanism": "Fosters humility and connection."
        },
        "rain": {
            "genre": "Devotional Marathi / Soulful Hindi",
            "acoustic_strategy": "Expansive vocal delivery, traditional instrumentation",
            "tracks": ["Ek Dil Ek Jaan", "Arziyaan"],
            "mechanism": "Induces humility and dissolves ego-driven superiority."
        },
        "fog": {
            "genre": "Indie / Vulnerable Acoustic",
            "acoustic_strategy": "Ethereal textures and raw lyrics",
            "tracks": ["How to Disappear Completely", "Sarajevo - Watsky"],
            "mechanism": "Provides safe space for regret and dismantling emotional walls."
        },
        "any": {
            "genre": "Warm R&B / Lyrical Self-care",
            "acoustic_strategy": "Comforting chord progressions and affirming lyrics",
            "tracks": ["Put Your Records On"],
            "mechanism": "Promotes relaxed acceptance of present moment."
        }
    }
}

# --- helper: example inference from Ambee response JSON ---
def infer_weather_key_from_ambee(ambee_response: dict) -> str:
    """
    Example logic to map an Ambee response JSON to one of the dictionary keys.
    ambee_response is expected to be the JSON returned by Ambee /weather/latest/by-lat-lng.

    Priority:
      1) If 'icon' present -> use it (maps directly to clear/cloudy/rain/fog/snow/partly-cloudy)
      2) If precipitation intensity > threshold -> 'rain' or 'thunderstorm' (use severe-storms endpoint or lightning flag if present)
      3) If visibility is very low -> 'fog'
      4) If 'summary' string contains keyword thunder/lightning/hail -> 'thunderstorm'
      5) fallback -> 'any'
    """
    if not ambee_response or not isinstance(ambee_response, dict):
        return "any"

    # 1) direct icon
    icon = ambee_response.get("icon") or ambee_response.get("weather", {}).get("icon")
    if icon:
        # normalize known values
        icon = icon.lower()
        if icon in AMBEE_WEATHER_KEYS:
            return icon
        # some responses use 'clear-day' / 'clear-night' or 'clear_day' variants
        if "clear" in icon:
            return "clear"
        if "cloud" in icon:
            # decide between partly-cloudy and cloudy by cloud_cover if present
            cloud_cover = ambee_response.get("cloudCover") or ambee_response.get("cloud_cover") or ambee_response.get("clouds")
            try:
                if cloud_cover is not None and float(cloud_cover) >= 0.6:
                    return "cloudy"
            except Exception:
                pass
            return "partly-cloudy"
        if "rain" in icon or "drizzle" in icon:
            return "rain"
        if "snow" in icon:
            return "snow"
        if "fog" in icon or "mist" in icon:
            return "fog"

    # 2) precipitation intensity (names vary by API; adapt to your response keys)
    precip = ambee_response.get("precipitationIntensity") or ambee_response.get("precipIntensity") or ambee_response.get("rain")
    if precip:
        try:
            # low values -> drizzle-like, high -> rain
            val = float(precip)
            if val > 5.0:
                return "rain"
            if val > 0.1:
                return "rain"
        except Exception:
            pass

    # 3) visibility -> fog
    visibility = ambee_response.get("visibility")
    if visibility is not None:
        try:
            if float(visibility) < 2000:  # meters threshold
                return "fog"
        except Exception:
            pass

    # 4) summary keyword search
    summary = (ambee_response.get("summary") or "").lower()
    if "thunder" in summary or "lightning" in summary:
        return "thunderstorm"
    if "snow" in summary:
        return "snow"
    if "rain" in summary or "drizzle" in summary:
        return "rain"
    if "fog" in summary or "mist" in summary or "haze" in summary:
        return "fog"
    if "clear" in summary:
        return "clear"
    if "cloud" in summary:
        return "partly-cloudy"

    # fallback
    return "any"