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

**live-peers** (28)
```bash
peers="ba49814ebe24e4d1ba41f4fc774997bd5d7d8e47@65.108.126.46:35656,30a63eaa77f7f95d741d16c2564441c4422fdb25@185.219.142.120:26656,0bde2942c047313fd7f47e599040cd57cf503237@86.48.5.92:26656,2a16235c87399b714877872b9ab0ab1f7c0b063b@185.245.183.55:26656,8279e11d79bb4d5ee3595893a546123423e48b6a@109.123.246.138:26656,c84610dc61c7a7577705137437e1e655936cdd4f@85.114.142.4:39656,1587dd54b6e1f373ccf61401980816fbd7f7e43a@35.232.147.245:26656,74c99f232d4641876a51bf1dd609c5c6d0dd92a9@178.127.251.158:26656,104a00413d0fc7ec208c810c50d49932da355bd5@129.226.159.141:26656,a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656,f46e6fc8434bdbc034b5f7c07f2e5eca95f7e5bb@95.31.253.40:26656,ac74cb4cc17470f39a575699d4979317315cacac@185.196.20.6:26656,3edbefe333daf987dea52dd53e776add12483e70@193.203.15.44:26656,7eadee0a0fce081e7d9e786da806876d3d15383b@91.166.97.88:26656,a3de1f505133b416a47f546b4d4ccbdc442a891b@84.46.251.68:26656,2294ce01431e5a2b6624e6a1ac4617f794ff0b93@185.197.250.186:26656,b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,e709c3a1dcf3514d427fee196e12aa5b77e1f452@65.109.175.175:26656,766f17b24c11b5eac20cf938f619bc2e43331988@38.242.229.238:26656,f0d751eff5ea003019f66c47cf342f9e29c5b9cd@142.93.199.34:26656,637c4d2a687384db43a6859cf977f3c8006fdd2e@159.69.68.42:56656,2d9c1b81edeb8bf8630c0bea241f897f437b1ef0@195.162.79.17:26656,0681e865307756c8ac0832d128f00cde11576f37@88.210.13.198:26656,64fc57fb297ef839da5212b391cf27b32fe7ab8a@109.123.243.55:26656,01dfe6c993e034169d5e69116e64587fdaf0c2f1@93.183.208.67:26656,75dd6576eca67539ff92363c9afcf13338c3edd6@84.46.247.255:26656,bd4e84bd7b14201661c958c6cb6a1de2a27078ed@95.217.156.62:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
