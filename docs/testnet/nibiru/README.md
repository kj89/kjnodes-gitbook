# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nibiru.png" width="150" alt=""><figcaption></figcaption></figure>

Nibiru is a sovereign proof-of-stake blockchain, open-source platform,  and member of a family of interconnected blockchains that comprise the Cosmos Ecosystem.

**Chain ID**: nibiru-itn-1 | **Latest Version Tag**: v0.19.2 | **Wasm**: OFF

[Website](https://nibiru.fi) | [Discord](https://discord.gg/nibiru) | [Twitter](https://twitter.com/NibiruChain)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/nibiru-testnet](https://explorer.kjnodes.com/nibiru-testnet)

## Public endpoints

* api: [https://nibiru-testnet.api.kjnodes.com](https://nibiru-testnet.api.kjnodes.com)
* rpc: [https://nibiru-testnet.rpc.kjnodes.com](https://nibiru-testnet.rpc.kjnodes.com)
* grpc: nibiru-testnet.grpc.kjnodes.com:39090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nibiru-testnet.rpc.kjnodes.com:39656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nibiru-testnet.rpc.kjnodes.com:39659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nibiru-testnet/addrbook.json > $HOME/.nibid/config/addrbook.json
```

**live-peers** (24)
```bash
peers="a3de1f505133b416a47f546b4d4ccbdc442a891b@84.46.251.68:26656,30abc253688f7e70a6dcae9f0850e41a0245db3a@129.226.148.203:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,104a00413d0fc7ec208c810c50d49932da355bd5@129.226.159.141:26656,f4fa2e13e64628d96f9158a6a2afbb19ebac574e@85.190.246.120:26656,90e1f35289a3e527e04b59a53c1baeb4d02bdb63@65.108.94.198:26656,1587dd54b6e1f373ccf61401980816fbd7f7e43a@35.232.147.245:26656,b253cc6155ec59ea623f3f453d2f5a4b9c6d08fc@212.15.59.91:39656,bba542ac58a721585675a3ba35d5356d8b435b4f@45.67.217.201:26656,2a379d321d668f2bc10a2ab661b261c397bc78bb@185.197.194.233:26656,9dde137d2a59bf24dd25fc2be78a56183ac56bbb@109.123.246.117:26656,4a6bfd01b4ee7ba262e303236ad5a6514fc93ce1@31.220.89.144:26656,971fa24215b57d81be85a68a0a85b0b64d122dfc@5.166.240.95:26656,785ffb99f8724319d44254cbb47b3428aaaa25a5@38.242.236.134:26656,1309da8b18c31a63f6cb995f4b3facc2498b3bac@86.48.2.175:39656,76f44f79bba84e4473a3f89195a409e8d6eaf710@185.177.116.122:26656,7d3867934f0664832f782e3579e30686b069c473@109.123.250.109:26656,261be3ba3853f43fc4cc1bcb8a191b690452d809@94.130.207.69:26656,639bf251f6fe8b1d11c322c40a44e1c0f6ebf3e7@82.208.23.171:26656,aac16ac16e941f944c3c911db963e23159c6d637@38.242.246.213:26656,fa4f01794333e5b60470e2e90ca11f5ba2bdddab@31.220.94.24:26656,10e3f31fd0cfa829edfa6f855053d1e3cd93662e@5.75.249.183:26656,433d9db92f9e366a2c8170c7fd862acfba0c5e4f@185.192.97.246:26656,da12ccc20e8f2cc5105687a228b57deab377bb3f@38.242.247.198:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
