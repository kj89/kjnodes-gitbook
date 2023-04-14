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
peers="7fa2f4bdbacaf4569621dc76b3e4df4c13b8710e@65.109.71.250:22656,5ffee90e41903f6fba29dc75446d536a02d626fe@65.108.232.150:18095,62246c0c33a1a5a9f0fb4b40ab45db39cab5c44f@165.22.199.234:26130,73be725377cc966d8da48f751085de4d1581b391@185.242.112.32:27651,7583038c5f21ef6ddb60692469cfd80c97dd585d@88.218.224.126:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:45656,c0e6bf4193accabc14171ce163e704dcec5ea5df@51.91.215.170:36095,c46be592341987eae20ac681cb08d2abcc02ab9a@137.74.4.20:2000,59bb909c57664fafe88bf1b6924769c15a769ba4@65.108.125.236:3000,d10e5704f3c8e9dd6ef42445e4b88bb57d0a8289@65.108.8.247:18556,b88814bddfccd85289d7201bfd6fc6c4b3342ab2@178.162.165.193:36095,ca5a76c51bbbc57f839e6ed08953d3926eaa6e5b@34.159.232.61:26656,d2a2c21754be65ad4a4f1de1f6163f681a6e8af8@192.99.44.79:18556,be7d56127ef887d095b2f55f09be5fee1969d922@146.59.52.48:18095,6bcae846a2dc02b86ef6a0950655e65522da4e56@65.109.106.169:26656,76969af1bccdd4dcc511741b171c3d4ccb837ba6@146.59.85.223:18556,84f821d36d45cc0cdaa4ff05297e888bb0d9de8f@85.237.193.111:26656,d0dbb50a474888b8bed04bf8a23ac6b8bae443ee@5.79.79.80:18095,c3763808d3ed05c475b8a31cdd97fc522c088f4f@162.55.245.149:12020,e1b058e5cfa2b836ddaa496b10911da62dcf182e@65.21.136.170:55656,931f46cc338f59222c22565e216a16f57bbb9782@95.217.164.44:26656,969af6a39a0f7e8a17b92d90888360ad92248626@65.108.132.107:2000,04bd5d9511f40dd4bec23cc261d7838d9f8326cf@213.32.24.201:26656,7bcc2e490b6aa2536d68de0881cba2ee7134840c@139.59.8.48:26130,c06b9689397667fa060d8c3458dd391962d89be2@116.202.36.240:18556,88f8e4d74b70e18d4f3515d34701704086aa77e1@38.146.3.134:18556,c21bdeb3e1726428e7ec3a586b77242677f8fae5@38.146.3.135:18556,530b1964bc17bca6457311f1c2d5a2f3d25b297a@51.81.155.97:18556,ebc272824924ea1a27ea3183dd0b9ba713494f83@185.16.39.158:27056,86baedb502883a67947c84f62f3b6b89fc630988@107.155.81.98:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.mars/config/config.toml
```
