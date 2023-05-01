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
* grpc: nibiru-testnet.grpc.kjnodes.com:139090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nibiru-testnet.rpc.kjnodes.com:139656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nibiru-testnet.rpc.kjnodes.com:139659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nibiru-testnet/addrbook.json > $HOME/.nibid/config/addrbook.json
```

**live-peers** (26)
```bash
peers="b6fe0cb29a6cca2acd41aade05c46272db5c7c0c@209.126.83.209:26656,d2f53fd715b205d1321a22bad1a6334a06f3de2b@64.227.4.135:03656,5db2f2c82ba2b9c431d069270ebc16d35985ffaa@91.230.110.96:26656,6173aa0fb340ab41724d72339d164a86e7a6d0ac@185.229.119.95:26656,7685c50934491640cc4c082a687d4d7c140a0816@38.242.226.1:26656,7635811ac19bde0a542b76a403968ea85fa5f58a@94.250.201.202:26656,8aac7e7f0fdc0d71297be33e2081472434ae6d99@65.108.85.106:26656,0cc5236b8a37e89af65c8504982ae0eb5b01e004@178.20.47.61:26656,23d76c8b1e89958dea79f508f74c6866d2da7855@38.92.49.2:26656,31fa18ff28fd7f80d279a951849e4ef56003b039@128.140.85.113:26656,e3fc96a180861a923807d29b748a6cddd3230a8f@5.189.171.168:26656,5b2614774a890a7383e9700e4fc8fa202517ec74@144.91.97.6:26656,8c77970aa85235d543bfb26a47a332639dc89191@68.183.236.120:26656,cf13f41c223c6e47e581f6ae8ec7c554218de8fc@207.244.251.201:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,c51373e7a181c8b954d894bf356adcfe10c1c25b@89.58.16.33:36656,c709cad9e11b315644fe8f1d2e90c03c5cba685c@94.60.6.236:26656,6028bf33e78679aec8db8c7bcf8024705dd74b8e@95.216.148.212:26656,c20a499a21668237d67b44d44623aaebedbea81f@173.249.20.170:26656,9396be2fcf4f271496dffb8cd034d5a17e39dbcc@216.250.122.228:39656,b15395da25c90aa2d4fa3df2e3d767f1df3a3e09@86.48.2.245:26656,8eff5b8e877d4f48f6363468840d0265c18d500a@167.172.181.179:39656,b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,0945129df734538663010c1349f1b4f29da48687@89.117.48.176:26656,36c8b1ffb65f4455c864d891662642fb6c7458e4@176.9.76.130:26656,ab9cba0df8e49cbfcbd4f1b3bb85c0557930e36a@109.123.243.5:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
