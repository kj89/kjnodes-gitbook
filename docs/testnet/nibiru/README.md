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

**live-peers** (22)
```bash
peers="7e75b2249d088a4dfc3b33f386c316cb47366d2b@195.3.221.48:11656,b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,dd58949cab9bf75a42b556d04d3a4b1bbfadd8b5@144.76.97.251:40656,c20a499a21668237d67b44d44623aaebedbea81f@173.249.20.170:26656,790d36e7ea45d6660427d4c7473bac0ef525e78a@184.174.36.119:26656,97c4976b580a5ef4c3b82e239c50c81b8ab8189d@49.12.123.87:46656,a5455fdd70a915023bb4902143704430793c3e68@162.55.163.78:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,f98a8229e5dc6da6d5e49fd4e115472df3d1773c@95.9.36.100:26656,25e01aa86dae35ef0207991d1da02b7a9adf5e4a@38.242.219.103:26656,65a213efcad697afb5a1303c7fe5be4168d9520c@43.154.103.36:26656,db832cabda2d29d8e2570c0f3a5797098db5a7b8@135.181.25.101:26656,ba4533a60790009033673e66a53e53fc5db436e4@93.183.208.83:26656,05b0e8da493f0be9fd94350da52fb59c54cc897f@161.97.150.23:26656,a6062857b20b62693523643cb19dc0f3dd4ee961@90.188.249.252:26656,5e65a3d32678a7206d006f899be707c130a9ada1@162.55.234.70:55356,4af344bb3302bf926580f0b8ea4de9be401c3522@94.131.111.156:26656,b253cc6155ec59ea623f3f453d2f5a4b9c6d08fc@212.15.59.91:39656,20da1f2c82539b0e75e818d74cb3a3dd3f8e6b63@38.242.229.208:27656,88e1a734951a8a4ea3f0b533d8bb49b9a5c24fde@120.226.39.116:16656,86a9ef837a37446469fc424b66e8fbf10d6619aa@84.46.255.162:26656,d5d51ad6226922fe0a85de41e972722021e6b982@138.201.31.28:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
