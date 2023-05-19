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

**live-peers** (11)
```bash
peers="59bb909c57664fafe88bf1b6924769c15a769ba4@65.108.125.236:3000,b88814bddfccd85289d7201bfd6fc6c4b3342ab2@178.162.165.193:36095,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:14556,931f46cc338f59222c22565e216a16f57bbb9782@95.217.164.44:26656,695add58c0b9379f42b326977ffc4bc6d7fe2100@116.202.229.240:36656,d0dbb50a474888b8bed04bf8a23ac6b8bae443ee@5.79.79.80:18095,c0e6bf4193accabc14171ce163e704dcec5ea5df@51.91.215.170:36095,32af09a8b5723864cb30b0e69dc2b0e2e5cd63d0@193.26.159.34:26656,becb82a1fbd1b539a413f19967b5148a43bc4515@159.223.55.135:26656,e33a706b8060a025d2ab1061cbe8eae9fcc30e38@15.204.207.117:26656,9ceeff8c0ea31114d668fcf01fc2f74ea5037ba8@213.32.24.201:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.mars/config/config.toml
```
