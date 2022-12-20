# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/hypersign.png" width="150" alt=""><figcaption></figcaption></figure>

Hypersign is a decentralized identity layer for the internet, giving  users control of their personal data and identity whilst digital  enabling trust for businesses.

**Chain ID**: jagrat | **Latest Version Tag**: v0.1.5 | **Wasm**: OFF

Website: [https://hypersign.id](https://hypersign.id)


## Public endpoints

* rpc: [https://hypersign-testnet.rpc.kjnodes.com](https://hypersign-testnet.rpc.kjnodes.com)
* api: [https://hypersign-testnet.api.kjnodes.com](https://hypersign-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@hypersign-testnet.rpc.kjnodes.com:31656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@hypersign-testnet.rpc.kjnodes.com:31659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/hypersign-testnet/addrbook.json > $HOME/.hid-node/config/addrbook.json
```

**live-peers** (10)
```
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:31656,f277d5a80e789ce69bb3318dfd5efea45986c073@176.9.22.117:31656,7d85caec437cc8c0a504d6ab3b18fd07c173b2fb@94.130.219.37:26001,a275d8018f683f279bf5167a72d294bfacafa839@178.63.102.172:41656,1380864bb38481fef4b2358026a5ed53fc027679@95.214.52.206:26656,ce6686036f6554deb0490103dcc201172e7c3f2f@81.0.220.131:26656,d92268c246e02a54103f7098b901b876c88f006e@5.161.130.108:26656,2641ddcf28d8adf448edb573de1efba0b6971d9e@178.154.222.128:26656,52eee2c34150d621312087e49f118969472ba55f@149.102.137.192:26656,4aa182ce191cd089929544fe0612d33a02a2cde9@46.17.250.145:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.hid-node/config/config.toml
```
