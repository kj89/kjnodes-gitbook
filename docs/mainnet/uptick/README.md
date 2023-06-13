# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/uptick.png" alt=""><figcaption></figcaption></figure>

Uptick Network is building business-grade infrastructure and  ecosystems for non-fungible tokens (NFTs). The platform is  designed with a focus on multi-chain and cross-chain interoperability,  and includes three key components: the NFT infrastructure, an NFT  marketplace, and NFT ecosystem applications.

**Chain ID**: uptick_117-1 | **Latest Version Tag**: v0.2.8 | **Wasm**: OFF

[Website](https://uptick.network) | [Discord](https://discord.gg/UzeHS7fu5H) | [Twitter](https://twitter.com/uptickproject)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/uptick/uptickvaloper1jqpaf0vgzlxvjx5meq8huweuv2nguqe20seefq)

Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals

## Restake

[Restake with kjnodes](https://restake.app/uptick/uptickvaloper1jqpaf0vgzlxvjx5meq8huweuv2nguqe20seefq) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/uptick](https://explorer.kjnodes.com/uptick)

## Public endpoints

* api: [https://uptick.api.kjnodes.com](https://uptick.api.kjnodes.com)
* rpc: [https://uptick.rpc.kjnodes.com](https://uptick.rpc.kjnodes.com)
* grpc: uptick.grpc.kjnodes.com:11590

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@uptick.rpc.kjnodes.com:11556
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@uptick.rpc.kjnodes.com:11559
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/uptick/addrbook.json > $HOME/.uptickd/config/addrbook.json
```

**live-peers** (17)
```bash
peers="e88413ee7153be8a9053165a60ad55492a8e300a@65.109.94.250:29656,7ac86e61608b3d44bb0941a8fbb844e5772db984@65.108.69.17:10656,a5408575fc327823f73c153d9f89c932ac30a335@141.94.141.144:28056,1160d5e94fbce4f8ccabb0203344c673f3af3fb6@141.94.139.233:27656,ea83a93c2878af90d034138fc5026218fb89d0d2@69.197.19.36:21656,f05733da50967e3955e11665b1901d36291dfaee@65.108.195.30:21656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11556,46900f4eb164f31967963544e4d9e7aac0d08a08@107.155.125.186:15656,b2bcb66f270153791b19e16ff23ddfec096f7097@142.132.202.50:41656,29269b318b35005b4ac39d010cbc3c41a5ab0833@185.144.99.33:26656,03d4bd74d72794fefc260008943d48dc502b7518@65.108.232.168:34656,f2710fe78495a0645b690dbf9296b5d62bc2a39f@148.113.6.229:20456,250c98d4975ae9a12ed7dfcd5a7cf76b470e49a6@65.21.108.180:26656,34d86f3a8dfce7d8b615563c587433c65792f104@185.219.142.221:15656,90c0c03d27e5b4354bffb709d28340f2657ca1c7@138.201.121.185:26679,e71bae28852a0b603f7360ec17fe91e7f065f324@142.132.253.112:35656,f97a75fb69d3a5fe893dca7c8d238ccc0bd66a8f@142.132.148.140:6969"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.uptickd/config/config.toml
```
