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

**live-peers** (18)
```bash
peers="07933f8021f92499457890184ae228cd4a2a52fb@65.21.90.141:26656,f05733da50967e3955e11665b1901d36291dfaee@65.108.195.30:21656,ee045c74c0678f1122650a3a5223923977cae1b3@65.109.93.152:30656,024a9c6eb41193e7fc76544572c0a8370e80e953@65.109.92.240:3156,03d4bd74d72794fefc260008943d48dc502b7518@65.108.232.168:34656,4914c40a9441895f355c600f38ed94756782ab99@146.59.81.204:27856,34d86f3a8dfce7d8b615563c587433c65792f104@185.219.142.221:15656,81ccbba5cba98cf89bcca74f271380b53afed4c4@154.26.130.207:27656,6ba2d2664d0398fee52c08b13d6592fce4ee56ad@144.126.140.255:15656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:15656,bb6aaef7667af68862ee582085c2e9dd2b568d86@54.254.135.200:26656,48e7e8ca23b636f124e70092f4ba93f98606f604@54.37.129.164:55056,e8704845eaa0f3d39fcdc9c4065f3beb344384db@142.132.152.46:27656,632c2362378546ab77883077861f38405c378d06@104.194.8.68:60556,b45ee634889abf61c7212b03dbddb853a8a3bc09@185.48.24.112:15656,038aca614e49ec4e5e3a06c875976a94c478cb09@65.108.195.29:21656,12a02a775eb43f3f0becce037ae4403b3ae4b43d@94.130.16.254:56656,0b730506f313e19ae3b7d2815a33558ecefec066@45.85.147.42:17656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.uptickd/config/config.toml
```
