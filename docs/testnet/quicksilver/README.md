# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/quicksilver.png" width="150" alt=""><figcaption></figcaption></figure>

Quicksilver is a permissionless, sovereign Cosmos SDK zone providing liquid staking for the entire Cosmos Ecosystem.

**Chain ID**: innuendo-3 | **Latest Binary Version**: v0.10.2 | **Wasm**: OFF

Website: [https://quicksilver.zone](https://quicksilver.zone)


## Public endpoints

* rpc: [https://quicksilver-testnet.rpc.kjnodes.com](https://quicksilver-testnet.rpc.kjnodes.com)
* api: [https://quicksilver-testnet.api.kjnodes.com](https://quicksilver-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@quicksilver-testnet.rpc.kjnodes.com:11656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@quicksilver-testnet.rpc.kjnodes.com:11659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/quicksilver-testnet/addrbook.json > $HOME/.quicksilverd/config/addrbook.json
```

**live-peers** (10)
```
peers="433f85361545a434ad6b4202e2f373e4894ecf39@142.132.151.99:15619,66f9d8f52a4637dc9215cdaa8dc2977633e52bbf@95.217.144.121:26656,2096650d8586b858d3369205f3b46ac4c765bc8e@65.109.53.155:26656,8ff8a186fe9cbc70d0f34891fa051f87e561a48b@158.160.0.93:26656,7c65eaf6307530cc654d62fff271a9593643758b@23.227.200.10:26656,125327a98d0e63adfb3f0be513947a96b24231fa@5.161.145.173:26656,7b21198feaf0882f09fcbb24060961f434d158a3@35.242.163.107:26656,ebafa16e082c52d5b74ee770d6ebf5666cee9ca6@167.99.184.76:26656,0a3ac40a7a4ce35978c4da97be2eb6974bc3c58b@185.252.233.217:46656,c896ef12812a82eea865111c49f226849ad077db@144.76.236.90:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.quicksilverd/config/config.toml
```
