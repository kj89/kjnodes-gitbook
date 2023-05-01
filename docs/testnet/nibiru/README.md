# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nibiru.png" alt=""><figcaption></figcaption></figure>

Nibiru is a sovereign proof-of-stake blockchain, open-source platform,  and member of a family of interconnected blockchains that comprise the Cosmos Ecosystem.

**Chain ID**: nibiru-itn-1 | **Latest Version Tag**: v0.19.2 | **Wasm**: OFF

[Website](https://nibiru.fi) | [Discord](https://discord.gg/nibirufi) | [Twitter](https://twitter.com/NibiruChain)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/nibiru-testnet](https://explorer.kjnodes.com/nibiru-testnet)

## Public endpoints

* api: [https://nibiru-testnet.api.kjnodes.com](https://nibiru-testnet.api.kjnodes.com)
* rpc: [https://nibiru-testnet.rpc.kjnodes.com](https://nibiru-testnet.rpc.kjnodes.com)
* grpc: nibiru-testnet.grpc.kjnodes.com:13990

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nibiru-testnet.rpc.kjnodes.com:13956
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nibiru-testnet.rpc.kjnodes.com:13959
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nibiru-testnet/addrbook.json > $HOME/.nibid/config/addrbook.json
```

**live-peers** (25)
```bash
peers="19fd0e304b15b5ce7abbbf27779eac77ca08fc23@65.109.157.236:46656,d2f53fd715b205d1321a22bad1a6334a06f3de2b@64.227.4.135:03656,c51373e7a181c8b954d894bf356adcfe10c1c25b@89.58.16.33:36656,2ce838eea29c3f6ca650081dd0fa99186304b151@37.99.82.28:26656,a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656,0945129df734538663010c1349f1b4f29da48687@89.117.48.176:26656,c709cad9e11b315644fe8f1d2e90c03c5cba685c@94.60.6.236:26656,5db2f2c82ba2b9c431d069270ebc16d35985ffaa@91.230.110.96:26656,7685c50934491640cc4c082a687d4d7c140a0816@38.242.226.1:26656,a34c137b631a8c55c4dd51bf02823ab8eedc6020@89.117.51.194:26656,e88d5df5ea0c26dca6259564bf15934615012bd3@84.46.240.144:39656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,cf13f41c223c6e47e581f6ae8ec7c554218de8fc@207.244.251.201:26656,36c8b1ffb65f4455c864d891662642fb6c7458e4@176.9.76.130:26656,e3fc96a180861a923807d29b748a6cddd3230a8f@5.189.171.168:26656,03833de20845507fd9c6d2ac1797d28ef4528b0c@109.123.252.252:26656,86a9ef837a37446469fc424b66e8fbf10d6619aa@84.46.255.162:26656,aaff99ce425ac9d062d1bca6f75987656e137307@138.201.34.19:26656,d0b30b6fdd2df3e70e41fb0ba43b400e7d02e6e0@38.242.252.252:26656,512d47ba933acf49081ebeb4a41317694f057e3d@94.131.15.62:26656,65a213efcad697afb5a1303c7fe5be4168d9520c@43.154.103.36:26656,51b6186857ffd7adf4ed0c5a080cfe882299b046@94.124.78.129:26656,c653964fd9adb62e4f775aa673f3a9d568ac0e14@109.123.229.224:26656,f98a8229e5dc6da6d5e49fd4e115472df3d1773c@95.9.36.100:26656,8c77970aa85235d543bfb26a47a332639dc89191@68.183.236.120:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
