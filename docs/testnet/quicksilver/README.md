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

**live-peers** (20)
```
peers="13564ca7ffcc8fa6bcc6d405c96fe8c724ec17da@88.99.213.25:11656,d4d83e209a2b096859821228ea17475f9a487a48@23.88.0.170:15651,c896ef12812a82eea865111c49f226849ad077db@144.76.236.90:26656,af8cfa944802a9bd510fc3407950a15e8be86c31@213.239.217.52:30656,41f7d7004cace7bd1760a5f980a86123700c8f1d@185.146.148.116:26656,c9a74cdd754a8ccc9243ac2b245e4caaa78695aa@45.85.147.96:26656,3da9fbcb9ec210ec1c94ebc49f46fad3d3721e77@65.108.136.39:26651,66f9d8f52a4637dc9215cdaa8dc2977633e52bbf@95.217.144.121:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:11656,bdb93c655989b2c1882339fabb013317066dda56@95.214.52.138:26676,8ff8a186fe9cbc70d0f34891fa051f87e561a48b@158.160.0.93:26656,1c1ca90d704c22844570d57039ccf2e8f58e475d@80.64.208.123:26656,7c65eaf6307530cc654d62fff271a9593643758b@23.227.200.10:26656,8a334ed2e728ca1164f8ef6ae58dd5fda31da5be@66.94.104.239:26641,6c31ea769b18d7b20b2d738df7778fb9fc3fc380@18.236.225.32:26656,858ba6bc33a6d13fdd9ddad344d788dcf91cf565@142.132.151.99:15651,2096650d8586b858d3369205f3b46ac4c765bc8e@65.109.53.155:26656,5844010472bac487748336616d450bc9f0cbc57c@65.108.72.175:29656,a37474c1f254cd4b16d924327a755c914e8e7d86@65.109.30.53:26656,e0f0703e9ce343c46e0ec01b19216715e817b358@65.109.85.170:28656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.quicksilverd/config/config.toml
```
