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

**live-peers** (21)
```
peers="d4d83e209a2b096859821228ea17475f9a487a48@23.88.0.170:15651,c896ef12812a82eea865111c49f226849ad077db@144.76.236.90:26656,13564ca7ffcc8fa6bcc6d405c96fe8c724ec17da@88.99.213.25:11656,41f7d7004cace7bd1760a5f980a86123700c8f1d@185.146.148.116:26656,c9a74cdd754a8ccc9243ac2b245e4caaa78695aa@45.85.147.96:26656,e0f0703e9ce343c46e0ec01b19216715e817b358@65.109.85.170:28656,66f9d8f52a4637dc9215cdaa8dc2977633e52bbf@95.217.144.121:26656,b9b8bb23e61d53ff3b293485d04ea567ebcd7933@65.108.65.94:26656,8099f8a7c95c1676982e1a23e8452f2b10b07415@65.108.78.107:22656,3da9fbcb9ec210ec1c94ebc49f46fad3d3721e77@65.108.136.39:26651,2096650d8586b858d3369205f3b46ac4c765bc8e@65.109.53.155:26656,8a334ed2e728ca1164f8ef6ae58dd5fda31da5be@66.94.104.239:26641,7c65eaf6307530cc654d62fff271a9593643758b@23.227.200.10:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:11656,af8cfa944802a9bd510fc3407950a15e8be86c31@213.239.217.52:30656,ca1dc45c25919c5b945f4c52c1e8470755a01225@65.108.44.149:20656,532625a997a6f891405202968607f72afe004f15@202.61.225.157:26666,8ff8a186fe9cbc70d0f34891fa051f87e561a48b@158.160.0.93:26656,bdb93c655989b2c1882339fabb013317066dda56@95.214.52.138:26676,a37474c1f254cd4b16d924327a755c914e8e7d86@65.109.30.53:26656,7781c28c240e85474425040f744b501d99120d1d@195.201.108.152:11656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.quicksilverd/config/config.toml
```
