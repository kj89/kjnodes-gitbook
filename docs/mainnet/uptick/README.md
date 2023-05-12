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

**live-peers** (21)
```bash
peers="ee045c74c0678f1122650a3a5223923977cae1b3@65.109.93.152:30656,8d9bfdb1e2657959ec641828080052d554fbe248@65.108.205.47:36656,90c0c03d27e5b4354bffb709d28340f2657ca1c7@138.201.121.185:26679,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11556,8ecd3260a19d2b112f6a84e0c091640744ec40c5@185.165.241.20:26656,5a1fd15ecac0124ecf143cd003dad232d41a0e2e@62.171.158.177:35656,f2710fe78495a0645b690dbf9296b5d62bc2a39f@148.113.6.229:20456,f05733da50967e3955e11665b1901d36291dfaee@65.108.195.30:21656,a5408575fc327823f73c153d9f89c932ac30a335@141.94.141.144:28056,1160d5e94fbce4f8ccabb0203344c673f3af3fb6@141.94.139.233:27656,78017b785ef1f781a1f4090f9ecf4adb2b476ab9@217.197.117.53:36656,d0938452e1d0fd039232c4247076634a01f601e5@83.171.249.159:31656,ffd85619e0baed6ad09eec1e9c1651ded8e00b3b@82.165.186.119:26656,e6eb810c0495bc3c9e562f92b349458e7c5ec073@18.138.220.30:26656,4914c40a9441895f355c600f38ed94756782ab99@146.59.81.204:27856,755c376ec8df0c6fce6d3e28f3d9054de4fe456f@81.30.157.35:17656,e213d0a9c203c45e8bf89bd2247b1ba1d2b3691b@185.239.208.131:31656,e71bae28852a0b603f7360ec17fe91e7f065f324@142.132.253.112:35656,b45ee634889abf61c7212b03dbddb853a8a3bc09@185.48.24.112:15656,34d28eeb7be1b245fd64ba2df4cdf62b5eb60dd3@202.61.240.155:30001,34d86f3a8dfce7d8b615563c587433c65792f104@185.219.142.221:15656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.uptickd/config/config.toml
```
