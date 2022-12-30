# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/quicksilver.png" width="150" alt=""><figcaption></figcaption></figure>

Quicksilver is a permissionless, sovereign Cosmos SDK zone providing liquid staking for the entire Cosmos Ecosystem.

**Chain ID**: innuendo-4 | **Latest Version Tag**: ${LATEST_VERSION_TAG} | **Wasm**: OFF

[Website](https://quicksilver.zone) | [Discord](https://discord.gg/quicksilverprotocol) | [Twitter](https://twitter.com/quicksilverzone)


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

**live-peers** (7)
```
peers="cfbf02b41e7fe78d51abfa93f342afd0687203c0@212.227.151.143:36656,858ba6bc33a6d13fdd9ddad344d788dcf91cf565@142.132.151.99:15651,fd10105bbfaaf9d45aafe13a34cdaed9cdca239d@51.89.7.235:26650,c4489720ba051c79f5bb16ae5d81341b0f248e19@34.240.190.194:26656,8ff8a186fe9cbc70d0f34891fa051f87e561a48b@158.160.0.93:26656,8a334ed2e728ca1164f8ef6ae58dd5fda31da5be@66.94.104.239:26641,d4d83e209a2b096859821228ea17475f9a487a48@23.88.0.170:15651"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.quicksilverd/config/config.toml
```
