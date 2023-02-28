# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/mars.png" width="150" alt=""><figcaption></figcaption></figure>

Mars is a credit protocol for the future: non-custodial,  open-source, transparent, algorithmic and community-governed.

**Chain ID**: mars-1 | **Latest Version Tag**: v1.0.0 | **Wasm**: ON

[Website](https://marsprotocol.io) | [Discord](https://discord.gg/marsprotocol) | [Twitter](https://twitter.com/mars_protocol)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/mars/marsvaloper1p9t4gr40rnpdwqacxgcqp7ffrfw908nu020g4n)

## Restake

[Restake with kjnodes](https://restake.app/mars/marsvaloper1p9t4gr40rnpdwqacxgcqp7ffrfw908nu020g4n) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/mars](https://explorer.kjnodes.com/mars)

## Public endpoints

* api: [https://mars.api.kjnodes.com](https://mars.api.kjnodes.com)
* rpc: [https://mars.rpc.kjnodes.com](https://mars.rpc.kjnodes.com)
* grpc: [https://mars.grpc.kjnodes.com](https://mars.grpc.kjnodes.com)

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

**live-peers** (19)
```bash
peers="5ffee90e41903f6fba29dc75446d536a02d626fe@65.108.232.150:18095,89757803f40da51678451735445ad40d5b15e059@169.155.44.75:26656,ef7c6b0f2ddfcef34a7f36681eaa8159be83b71f@178.128.28.236:26656,a57468bf54407d75dee78b0cb6612805c4ac83e1@45.85.147.42:13656,c46be592341987eae20ac681cb08d2abcc02ab9a@137.74.4.20:2000,d2a2c21754be65ad4a4f1de1f6163f681a6e8af8@192.99.44.79:18556,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:45656,969af6a39a0f7e8a17b92d90888360ad92248626@65.108.132.107:2000,c0e6bf4193accabc14171ce163e704dcec5ea5df@51.91.215.170:36095,141f6066694776b73ec6fc34356fe842ecf03898@46.38.243.16:45656,3e1d0c796a49b1315d95d336715fe0cad0470f40@195.189.96.106:42656,1193253f91a64aa3980df627d20f620c4cbb5ec5@34.83.213.40:26656,9e7f28b8c0ac9d8d17bb17a390421d540a29eb3f@154.26.158.158:18556,530b1964bc17bca6457311f1c2d5a2f3d25b297a@51.81.155.97:18556,c5bbf2507356483b05ad7feb8d42ff96c7bc5f03@80.64.208.174:26656,38edf28452ebc41f661d91b6613563c864f4c72e@35.228.114.46:26656,e1b058e5cfa2b836ddaa496b10911da62dcf182e@65.21.136.170:55656,be7d56127ef887d095b2f55f09be5fee1969d922@146.59.52.48:18095,b88814bddfccd85289d7201bfd6fc6c4b3342ab2@178.162.165.193:36095"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.mars/config/config.toml
```
