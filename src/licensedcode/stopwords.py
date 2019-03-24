# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 nexB Inc. and others. All rights reserved.
# http://nexb.com and https://github.com/nexB/scancode-toolkit/
# The ScanCode software is licensed under the Apache License version 2.0.
# Data generated with ScanCode require an acknowledgment.
# ScanCode is a trademark of nexB Inc.
#
# You may not use this software except in compliance with the License.
# You may obtain a copy of the License at: http://apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
#
# When you publish or redistribute any data created with ScanCode or any ScanCode
# derivative work, you must accompany this data with the following acknowledgment:
#
#  Generated with ScanCode and provided on an "AS IS" BASIS, WITHOUT WARRANTIES
#  OR CONDITIONS OF ANY KIND, either express or implied. No content created from
#  ScanCode should be considered or used as legal advice. Consult an Attorney
#  for any legal advice.
#  ScanCode is a free software code scanning tool from nexB Inc. and others.
#  Visit https://github.com/nexB/scancode-toolkit/ for support and download.

from __future__ import absolute_import
from __future__ import print_function


STOPWORDS = frozenset({
# common XML character references as &quot;
    'quot',
    'apos',
    'lt',
    'gt',
    'amp',
    'nbsp',

# common html tags as <a href=https://link ...> dfsdfsdf</a>
    'a',
    'href',
    'p',
    'br',
    'div',
    'em',
    'span',
    'class',
    'pre',
    'list',  # also a comment prefix
    'ul',
    'ol',
    'li',
    'tr',
    'td',
    'th',
    'img',
    'src',
    'h1',
    'h2',
    'h3',
    'h4',
    'h5',
    'blockquote',
    'body',
    'id',

# debian copyright files <s> tags
    's',

# comment line markers
    # batch files
    'rem',
    # autotools
    'dnl',

# doc book tags as <para>
    'ulink',
    'para',

# Some HTML punctuations and entities all as &emdash;
    'ge',
    'le',
    'emdash',  # rare and weird
    'mdash',
    'ndash',
    'bdquo',
    'ldquo',
    'ldquor',
    'lsaquo',
    'lsquo',
    'lsquor',
    'raquo',
    'rdquo',
    'rdquor',
    'rsaquo',
    'rsquo',
    'rsquor',
    'sbquo',
    'lpar',
    'rpar',
    'comma',
    'period',
    'colon',
    'semi',
    'tilde',
    'emsp',
    'ensp',
    'numsp',
    'puncsp',
    'thinsp',
    'hairsp',
    'bull',
    'bullet',
})



# query breaks
# in Android generated NOTICE.html files
breaks = {
    '<pre class="license-text">',
    '</pre><!-- license-text -->',
    '-------------------------------------------------------------------',
    '==============================================================================',
}


# TODO: use me?
# translations of HTML entities to words or letters
{
    '&eacute': 'e',
    '&copy': '(c)',
}
