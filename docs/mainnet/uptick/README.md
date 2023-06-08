# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/uptick.png" alt=""><figcaption></figcaption></figure>

Uptick Network is building business-grade infrastructure and  ecosystems for non-fungible tokens (NFTs). The platform is  designed with a focus on multi-chain and cross-chain interoperability,  and includes three key components: the NFT infrastructure, an NFT  marketplace, and NFT ecosystem applications.

**Chain ID**: uptick_117-1 | **Latest Version Tag**: v0.2.4 | **Wasm**: OFF

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

**live-peers** (20)
```bash
peers="7ac86e61608b3d44bb0941a8fbb844e5772db984@65.108.69.17:10656,b45ee634889abf61c7212b03dbddb853a8a3bc09@185.48.24.112:15656,29269b318b35005b4ac39d010cbc3c41a5ab0833@185.144.99.33:26656,f2710fe78495a0645b690dbf9296b5d62bc2a39f@148.113.6.229:20456,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11556,03d4bd74d72794fefc260008943d48dc502b7518@65.108.232.168:34656,81ccbba5cba98cf89bcca74f271380b53afed4c4@154.26.130.207:27656,f05733da50967e3955e11665b1901d36291dfaee@65.108.195.30:21656,90c0c03d27e5b4354bffb709d28340f2657ca1c7@138.201.121.185:26679,bb6aaef7667af68862ee582085c2e9dd2b568d86@54.254.135.200:26656,0720f8f6cd1f1bf1c9549cdb10b920a1583d7675@182.253.224.66:10656,b2bcb66f270153791b19e16ff23ddfec096f7097@142.132.202.50:41656,8e924a598a06e29c9f84a0d68b6149f1524c1819@57.128.109.11:26656,cf94f8a5060fc7078ba50d2de277a9b787ee6e30@18.217.244.254:26656,e71bae28852a0b603f7360ec17fe91e7f065f324@142.132.253.112:35656,0ee24fc626159c1ee79257306838cda628695c7d@95.217.130.224:26656,661e4acbdb446e543e5e86831b5750df829bc0e0@162.55.245.211:26658,78017b785ef1f781a1f4090f9ecf4adb2b476ab9@217.197.117.53:36656,4ae1f6e820e5dc33dcb1d1304b8160d25bcc9b0b@89.39.106.78:16656,f97a75fb69d3a5fe893dca7c8d238ccc0bd66a8f@142.132.148.140:6969"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.uptickd/config/config.toml
```
