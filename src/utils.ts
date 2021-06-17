/**
* Ultroid - UserBot
* Copyright (C) 2020 TeamUltroid
*
* This file is a part of < https://github.com/MR-UNKNOWN-X/testing/ >
* PLease read the GNU Affero General Public License in
* <https://www.github.com/MR-UNKNOWN-X/testing/blob/main/LICENSE/>.
**/

export const getDuration = (time: string | number): string => {
    if (typeof (time) === 'string') {
        time = parseInt(time)
    }
    let min = Math.floor(time / 60);
    let sec = time - min * 60;
    return `${min}m ${sec}s`;
}