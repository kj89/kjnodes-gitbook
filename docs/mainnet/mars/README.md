# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/mars.png" width="150" alt=""><figcaption></figcaption></figure>

Mars is a credit protocol for the future: non-custodial,  open-source, transparent, algorithmic and community-governed.

**Chain ID**: mars-1 | **Latest Version Tag**: v1.0.0 | **Wasm**: ON

[Website](https://marsprotocol.io) | [Discord](https://discord.gg/marsprotocol) | [Twitter](https://twitter.com/mars_protocol)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/mars/marsvaloper1p9t4gr40rnpdwqacxgcqp7ffrfw908nu020g4n)

Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals

## Restake

[Restake with kjnodes](https://restake.app/mars/marsvaloper1p9t4gr40rnpdwqacxgcqp7ffrfw908nu020g4n) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/mars](https://explorer.kjnodes.com/mars)

## Public endpoints

* api: [https://mars.api.kjnodes.com](https://mars.api.kjnodes.com)
* rpc: [https://mars.rpc.kjnodes.com](https://mars.rpc.kjnodes.com)
* grpc: mars.grpc.kjnodes.com:45090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@mars.rpc.kjnodes.com:45656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@mars.rpc.kjnodes.com:45659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/mars/addrbook.json > $HOME/.mars/config/addrbook.json
```

**live-peers** (30)
```bash
peers="5ffee90e41903f6fba29dc75446d536a02d626fe@65.108.232.150:18095,c46be592341987eae20ac681cb08d2abcc02ab9a@137.74.4.20:2000,b88814bddfccd85289d7201bfd6fc6c4b3342ab2@178.162.165.193:36095,c0e6bf4193accabc14171ce163e704dcec5ea5df@51.91.215.170:36095,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:45656,73be725377cc966d8da48f751085de4d1581b391@185.242.112.32:27651,7583038c5f21ef6ddb60692469cfd80c97dd585d@88.218.224.126:26656,d6c36c298508090c1fe8a47e5bc7943b99b21e62@185.215.180.226:26656,89757803f40da51678451735445ad40d5b15e059@169.155.44.75:26656,be7d56127ef887d095b2f55f09be5fee1969d922@146.59.52.48:18095,6bcae846a2dc02b86ef6a0950655e65522da4e56@65.109.106.169:26656,76969af1bccdd4dcc511741b171c3d4ccb837ba6@146.59.85.223:18556,d0dbb50a474888b8bed04bf8a23ac6b8bae443ee@5.79.79.80:18095,84f821d36d45cc0cdaa4ff05297e888bb0d9de8f@85.237.193.111:26656,969af6a39a0f7e8a17b92d90888360ad92248626@65.108.132.107:2000,ca5a76c51bbbc57f839e6ed08953d3926eaa6e5b@34.159.232.61:26656,c3763808d3ed05c475b8a31cdd97fc522c088f4f@162.55.245.149:12020,59bb909c57664fafe88bf1b6924769c15a769ba4@65.108.125.236:3000,7bcc2e490b6aa2536d68de0881cba2ee7134840c@139.59.8.48:26130,62246c0c33a1a5a9f0fb4b40ab45db39cab5c44f@165.22.199.234:26130,10778ee2afc2d6a6451c4399f0a4fed978723a4c@78.46.109.138:23656,6cbdee8a3fd9dc83b8296275c96e5372dbc3b143@148.113.159.123:26656,f983785fc56c1eda751233550e13380bebd6a2fe@65.108.46.248:56656,e61f11c5b03400d3a99c066f951ed0888a2b64af@65.108.238.103:18556,d2a2c21754be65ad4a4f1de1f6163f681a6e8af8@192.99.44.79:18556,4131038cf7f74c76394788405cef2e2cd643b895@52.68.2.159:26656,c3c99a66c4c1d00e9ea32864b6a506fb20ab6525@46.4.11.118:26656,63f6703a58ee4d9235e78d961408869af25a8f83@65.109.31.114:2500,530b1964bc17bca6457311f1c2d5a2f3d25b297a@51.81.155.97:18556,ebc272824924ea1a27ea3183dd0b9ba713494f83@185.16.39.158:27056"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.mars/config/config.toml
```
