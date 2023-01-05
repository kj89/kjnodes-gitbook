# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/quicksilver.png" width="150" alt=""><figcaption></figcaption></figure>

Quicksilver is a permissionless, sovereign Cosmos SDK zone providing liquid staking for the entire Cosmos Ecosystem.

**Chain ID**: innuendo-4 | **Latest Version Tag**: v1.1.0-innuendo | **Wasm**: OFF

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

**live-peers** (32)
```
peers="c133c4c0c7034c8c345330f394984ad08092fc14@138.201.17.11:27656,fd10105bbfaaf9d45aafe13a34cdaed9cdca239d@51.89.7.235:26650,cfbf02b41e7fe78d51abfa93f342afd0687203c0@212.227.151.143:36656,d4d83e209a2b096859821228ea17475f9a487a48@23.88.0.170:15651,3519e61e653db97f5d1c7f1bec9b0072bca4d5fe@144.76.45.59:16656,4ccdccd18a480f13af85aa798356c1bf856f5c20@88.208.57.200:11656,0a3ac40a7a4ce35978c4da97be2eb6974bc3c58b@185.252.233.217:46656,41f7d7004cace7bd1760a5f980a86123700c8f1d@185.146.148.116:26656,b9b8bb23e61d53ff3b293485d04ea567ebcd7933@65.108.65.94:26656,025e1a9ba7e536e1db47569b55081f7adf6d2f9e@95.217.83.28:26636,2caa7ddd45818914e96f540d2fc71784826bc660@161.97.155.94:26656,46f97e49a49694aead28c27be2c19300f509e273@65.108.129.94:26656,2be586e675b0f55c96905cc83496861c64112f44@65.108.99.224:56656,3c48a780b85d248e34e63eca5d44c624f93d09d5@135.181.59.162:11156,e0f0703e9ce343c46e0ec01b19216715e817b358@65.109.85.170:28656,796e72ffc343c187cd5e8397c0c09c0671d228e0@185.16.39.51:26656,2096650d8586b858d3369205f3b46ac4c765bc8e@65.109.53.155:26656,5844010472bac487748336616d450bc9f0cbc57c@65.108.72.175:29656,c4489720ba051c79f5bb16ae5d81341b0f248e19@34.240.190.194:26656,c9a74cdd754a8ccc9243ac2b245e4caaa78695aa@45.85.147.96:26656,bdb93c655989b2c1882339fabb013317066dda56@95.214.52.138:26676,22a393fe9174c29081ad8aeaf14ce01b9a79d8c6@159.203.28.113:26656,13564ca7ffcc8fa6bcc6d405c96fe8c724ec17da@88.99.213.25:11656,66f9d8f52a4637dc9215cdaa8dc2977633e52bbf@95.217.144.121:26656,c409d9297f85d1290b4d6b208a1e66015c51434d@5.161.145.173:26656,97377c16946f8e1fa69e7c2c6b7feb32c2090f09@116.202.227.117:11656,03332cdbc3d354846a18992effbb8c20aa28f52a@65.21.133.125:28656,a37474c1f254cd4b16d924327a755c914e8e7d86@65.109.30.53:26656,858ba6bc33a6d13fdd9ddad344d788dcf91cf565@142.132.151.99:15651,8ff8a186fe9cbc70d0f34891fa051f87e561a48b@158.160.0.93:26656,78acdbabc08231765444b3143a222d433a5157e1@142.132.205.94:15651,ee6bae1a6d4a1e07f1e4bc7963cabedc6b73426e@94.130.137.119:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.quicksilverd/config/config.toml
```
