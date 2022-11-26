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
peers="a854277e77b0ac095e53156266cdc39ad4b13b2f@142.132.205.94:15619,433f85361545a434ad6b4202e2f373e4894ecf39@142.132.151.99:15619,13564ca7ffcc8fa6bcc6d405c96fe8c724ec17da@88.99.213.25:11656,0551eaa0db7097274410ee27a71672817e314b83@167.235.245.191:26656,c133c4c0c7034c8c345330f394984ad08092fc14@138.201.17.11:27656,c4489720ba051c79f5bb16ae5d81341b0f248e19@54.194.109.230:26656,8ff8a186fe9cbc70d0f34891fa051f87e561a48b@158.160.0.93:26656,7c65eaf6307530cc654d62fff271a9593643758b@23.227.200.10:26656,125327a98d0e63adfb3f0be513947a96b24231fa@5.161.145.173:26656,66f9d8f52a4637dc9215cdaa8dc2977633e52bbf@95.217.144.121:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.quicksilverd/config/config.toml
```
