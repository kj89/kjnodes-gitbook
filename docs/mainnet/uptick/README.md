# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/uptick.png" width="150" alt=""><figcaption></figcaption></figure>

Uptick Network is building business-grade infrastructure and  ecosystems for non-fungible tokens (NFTs). The platform is  designed with a focus on multi-chain and cross-chain interoperability,  and includes three key components: the NFT infrastructure, an NFT  marketplace, and NFT ecosystem applications.

**Chain ID**: uptick_117-1 | **Latest Version Tag**: v0.2.4 | **Wasm**: OFF

[Website](https://uptick.network) | [Discord](https://discord.gg/UzeHS7fu5H) | [Twitter](https://twitter.com/uptickproject)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


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

**live-peers** (14)
```bash
peers="e8704845eaa0f3d39fcdc9c4065f3beb344384db@142.132.152.46:27656,038aca614e49ec4e5e3a06c875976a94c478cb09@65.108.195.29:21656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:15656,0b730506f313e19ae3b7d2815a33558ecefec066@45.85.147.42:17656,12a02a775eb43f3f0becce037ae4403b3ae4b43d@94.130.16.254:56656,e88413ee7153be8a9053165a60ad55492a8e300a@65.109.94.250:29656,6ba2d2664d0398fee52c08b13d6592fce4ee56ad@144.126.140.255:15656,34d86f3a8dfce7d8b615563c587433c65792f104@185.219.142.221:15656,b45ee634889abf61c7212b03dbddb853a8a3bc09@185.48.24.112:15656,81ccbba5cba98cf89bcca74f271380b53afed4c4@154.26.130.207:27656,03d4bd74d72794fefc260008943d48dc502b7518@65.108.232.168:34656,ed3b757ceede1b7b100cdbaf98d46eb5eecad72e@51.178.76.46:26656,8ecd3260a19d2b112f6a84e0c091640744ec40c5@185.165.241.20:26656,7093d04fe734c0210168c200ffdf2a2ff2f544cc@65.108.6.45:60956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.uptickd/config/config.toml
```
