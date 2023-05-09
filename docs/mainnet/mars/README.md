# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/mars.png" alt=""><figcaption></figcaption></figure>

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
* grpc: mars.grpc.kjnodes.com:14590

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@mars.rpc.kjnodes.com:14556
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@mars.rpc.kjnodes.com:14559
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/mars/addrbook.json > $HOME/.mars/config/addrbook.json
```

**live-peers** (10)
```bash
peers="969af6a39a0f7e8a17b92d90888360ad92248626@65.108.132.107:2000,89757803f40da51678451735445ad40d5b15e059@169.155.44.75:26656,1892755333d2cc6f7ba97bda1b1c709ad4ab69cd@50.21.173.82:26656,84f821d36d45cc0cdaa4ff05297e888bb0d9de8f@85.237.193.111:26656,be7d56127ef887d095b2f55f09be5fee1969d922@146.59.52.48:18095,e61f11c5b03400d3a99c066f951ed0888a2b64af@65.108.238.103:18556,b88814bddfccd85289d7201bfd6fc6c4b3342ab2@178.162.165.193:36095,d8e92c3ca2daddef493d518b4e850af26ec4027b@199.85.208.186:26656,d0dbb50a474888b8bed04bf8a23ac6b8bae443ee@5.79.79.80:18095,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:14556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.mars/config/config.toml
```
