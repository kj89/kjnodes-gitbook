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
peers="4db44ebd58fed67d2a22ce06a395ce489415f498@5.75.197.137:26650,38edf28452ebc41f661d91b6613563c864f4c72e@35.228.114.46:26656,b88814bddfccd85289d7201bfd6fc6c4b3342ab2@178.162.165.193:36095,be7d56127ef887d095b2f55f09be5fee1969d922@146.59.52.48:18095,7f4be5f7db9b920e965197b65974f0e1e64749e4@144.126.128.128:26656,d2a2c21754be65ad4a4f1de1f6163f681a6e8af8@192.99.44.79:18556,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:45656,7bcc2e490b6aa2536d68de0881cba2ee7134840c@139.59.8.48:26130,76969af1bccdd4dcc511741b171c3d4ccb837ba6@146.59.85.223:18556,73be725377cc966d8da48f751085de4d1581b391@185.242.112.32:27651,7583038c5f21ef6ddb60692469cfd80c97dd585d@88.218.224.126:26656,84f821d36d45cc0cdaa4ff05297e888bb0d9de8f@85.237.193.111:26656,d0dbb50a474888b8bed04bf8a23ac6b8bae443ee@5.79.79.80:18095,530b1964bc17bca6457311f1c2d5a2f3d25b297a@51.81.155.97:18556,c3763808d3ed05c475b8a31cdd97fc522c088f4f@162.55.245.149:12020,c0e6bf4193accabc14171ce163e704dcec5ea5df@51.91.215.170:36095,c46be592341987eae20ac681cb08d2abcc02ab9a@137.74.4.20:2000,59bb909c57664fafe88bf1b6924769c15a769ba4@65.108.125.236:3000,52f792239ee6098457ecf1ff7402cd0b2529cea1@178.62.12.19:26656,62246c0c33a1a5a9f0fb4b40ab45db39cab5c44f@165.22.199.234:26130,ca5a76c51bbbc57f839e6ed08953d3926eaa6e5b@34.159.232.61:26656,8bdf870e0eece71e1a09a80f5995d6d5e830c763@65.109.106.169:26656,97e4468ac589eac505a800411c635b14511a61bb@134.65.194.206:26656,9c0c747a44919d645f74354fbe095337630b9eee@37.252.184.228:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@185.16.39.158:27056,9ff4348d44d91972faba184bb3f9ba56eb9f5fa3@178.239.197.172:26656,120a44a50f702717c259319caa2447c77621865f@3.39.103.198:26656,c3c99a66c4c1d00e9ea32864b6a506fb20ab6525@46.4.11.118:26656,1616af7456f519a0f2360adcad45d4bb9d39c92d@146.59.85.222:26656,969af6a39a0f7e8a17b92d90888360ad92248626@65.108.132.107:2000"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.mars/config/config.toml
```
