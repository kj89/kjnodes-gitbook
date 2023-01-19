# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/quicksilver.png" width="150" alt=""><figcaption></figcaption></figure>

Quicksilver is a permissionless, sovereign Cosmos SDK zone providing liquid staking for the entire Cosmos Ecosystem.

**Chain ID**: innuendo-5 | **Latest Version Tag**: v1.3.1 | **Wasm**: OFF

[Website](https://quicksilver.zone) | [Discord](https://discord.gg/quicksilverprotocol) | [Twitter](https://twitter.com/quicksilverzone)


## Public endpoints

* api: [https://quicksilver-testnet.api.kjnodes.com](https://quicksilver-testnet.api.kjnodes.com)
* rpc: [https://quicksilver-testnet.rpc.kjnodes.com](https://quicksilver-testnet.rpc.kjnodes.com)
* grpc: [https://quicksilver-testnet.grpc.kjnodes.com](https://quicksilver-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@quicksilver-testnet.rpc.kjnodes.com:11656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@quicksilver-testnet.rpc.kjnodes.com:11659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/quicksilver-testnet/addrbook.json > $HOME/.quicksilverd/config/addrbook.json
```

**live-peers** (31)
```bash
peers="13564ca7ffcc8fa6bcc6d405c96fe8c724ec17da@88.99.213.25:11656,c896ef12812a82eea865111c49f226849ad077db@144.76.236.90:26656,af8cfa944802a9bd510fc3407950a15e8be86c31@213.239.217.52:30656,9e0604571aa20314c2261d70b7d8823414702715@51.159.141.209:26656,df10d618cfc818e5943f5eefd81f4df265f8393e@207.180.243.64:11656,4ccdccd18a480f13af85aa798356c1bf856f5c20@88.208.57.200:11656,22a393fe9174c29081ad8aeaf14ce01b9a79d8c6@159.203.28.113:26656,8099f8a7c95c1676982e1a23e8452f2b10b07415@65.108.78.107:22656,d40a714c11ea3040495246fa0ba8439fcff8a139@176.9.146.72:11656,4c24df4acfbaaf22e5f6f3c4d11ecf02e8cc343f@195.3.220.48:26656,66f9d8f52a4637dc9215cdaa8dc2977633e52bbf@95.217.144.121:26656,e0f0703e9ce343c46e0ec01b19216715e817b358@65.109.85.170:28656,a37474c1f254cd4b16d924327a755c914e8e7d86@65.109.30.53:26656,74abcb5243d4ffc43de6ad1a288d8e50adcd467e@65.109.80.176:20656,a637b94cb989909cc182623748ef179b0659f148@65.109.23.114:11156,3519e61e653db97f5d1c7f1bec9b0072bca4d5fe@144.76.45.59:16656,521eabb3f5a0698476baf22c45aaef396399da10@135.181.183.93:24656,c133c4c0c7034c8c345330f394984ad08092fc14@138.201.17.11:27656,ee6bae1a6d4a1e07f1e4bc7963cabedc6b73426e@94.130.137.119:26656,a288baa951cbe92b253c01c3936d930af1d56424@5.161.142.236:26656,25410bff2fb7312d24c11b1e990507e5e3aa40b7@135.125.5.31:48656,78acdbabc08231765444b3143a222d433a5157e1@142.132.205.94:15651,0a3ac40a7a4ce35978c4da97be2eb6974bc3c58b@185.252.233.217:46656,d160a8908b44f2a44ce17e0be1f9056b58993b9c@65.21.139.170:21026,858ba6bc33a6d13fdd9ddad344d788dcf91cf565@142.132.151.99:15651,cfbf02b41e7fe78d51abfa93f342afd0687203c0@212.227.151.143:36656,67224ac7f52eac4db6bb0a8de0bf8fbc5e7e0069@199.204.45.23:10656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:11656,f7edad3ff5a85d039e7de12067c63064c5b42d63@46.4.121.72:11656,3c48a780b85d248e34e63eca5d44c624f93d09d5@135.181.59.162:11156,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.55.232:27026"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
