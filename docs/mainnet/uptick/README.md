# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/uptick.png" width="150" alt=""><figcaption></figcaption></figure>

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
* grpc: uptick.grpc.kjnodes.com:15090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@uptick.rpc.kjnodes.com:15656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@uptick.rpc.kjnodes.com:15659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/uptick/addrbook.json > $HOME/.uptickd/config/addrbook.json
```

**live-peers** (17)
```bash
peers="14ca9d73314dd519bc0b0be8511c88f85fe6873e@46.4.81.204:17656,4edc708046fe6909345d7cd25bda5bb0f078e1c3@141.94.193.28:55056,0b730506f313e19ae3b7d2815a33558ecefec066@45.85.147.42:17656,024a9c6eb41193e7fc76544572c0a8370e80e953@65.109.92.240:3156,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:15656,48e7e8ca23b636f124e70092f4ba93f98606f604@54.37.129.164:55056,038aca614e49ec4e5e3a06c875976a94c478cb09@65.108.195.29:21656,b45ee634889abf61c7212b03dbddb853a8a3bc09@185.48.24.112:15656,bb6aaef7667af68862ee582085c2e9dd2b568d86@54.254.135.200:26656,81ccbba5cba98cf89bcca74f271380b53afed4c4@154.26.130.207:27656,6ba2d2664d0398fee52c08b13d6592fce4ee56ad@144.126.140.255:15656,34d86f3a8dfce7d8b615563c587433c65792f104@185.219.142.221:15656,03d4bd74d72794fefc260008943d48dc502b7518@65.108.232.168:34656,e8704845eaa0f3d39fcdc9c4065f3beb344384db@142.132.152.46:27656,a5408575fc327823f73c153d9f89c932ac30a335@141.94.141.144:28056,ee045c74c0678f1122650a3a5223923977cae1b3@65.109.93.152:30656,34d28eeb7be1b245fd64ba2df4cdf62b5eb60dd3@202.61.240.155:30001"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.uptickd/config/config.toml
```
