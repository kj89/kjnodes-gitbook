# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/quicksilver.png" width="150" alt=""><figcaption></figcaption></figure>

Quicksilver is a permissionless, sovereign Cosmos SDK zone providing liquid staking for the entire Cosmos Ecosystem.

**Chain ID**: innuendo-3 | **Latest Version Tag**: v0.10.0

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

**live-peers**: 32
```
PEERS="a37474c1f254cd4b16d924327a755c914e8e7d86@65.109.30.53:26656,c133c4c0c7034c8c345330f394984ad08092fc14@138.201.17.11:27656,c896ef12812a82eea865111c49f226849ad077db@144.76.236.90:26656,41f7d7004cace7bd1760a5f980a86123700c8f1d@185.146.148.116:26656,8a334ed2e728ca1164f8ef6ae58dd5fda31da5be@66.94.104.239:26641,025e1a9ba7e536e1db47569b55081f7adf6d2f9e@95.217.83.28:26636,06ec5dee70a810d008885b167581807f0f0314aa@38.129.16.69:11656,0551eaa0db7097274410ee27a71672817e314b83@167.235.245.191:26656,0a3ac40a7a4ce35978c4da97be2eb6974bc3c58b@185.252.233.217:46656,8e9758a4ad29a1eb0a3343b192c5ee3509aac09e@185.163.64.156:26656,dc88be3a0075ce429a423237abe223a9528ce0df@65.108.204.119:31656,2096650d8586b858d3369205f3b46ac4c765bc8e@65.109.53.155:26656,8ff8a186fe9cbc70d0f34891fa051f87e561a48b@158.160.0.93:26656,a854277e77b0ac095e53156266cdc39ad4b13b2f@142.132.205.94:15619,64c58848cae4f3f1cb5d7700d3c225aa21536d28@142.132.155.252:47656,ba6c461874236d6dc95083886c8bd833d47d5c0a@195.3.221.13:46656,7fe3007cba4de49584cbdad9489ffecfc9651c57@65.108.79.246:26673,7d112277450f0a8ef1059e6b334c373a215726ea@23.88.0.170:15619,711b97aa5956c6ce95c05895faa6c3ad3c04d440@135.181.59.162:11156,e0f0703e9ce343c46e0ec01b19216715e817b358@65.109.85.170:28656,ca1dc45c25919c5b945f4c52c1e8470755a01225@65.108.44.149:20656,87d4e2b90141d5d52ed04387db4a46408c3fd66c@35.240.77.20:26656,433f85361545a434ad6b4202e2f373e4894ecf39@142.132.151.99:15619,19c724a6c0e00615b22fc307798fba9640259e45@135.181.137.120:47656,5c6bfcfd42e8a4cf7960cf8b1860eed3de17196d@65.108.75.237:2010,47a7fac621a79649519eadbb8deb92d33bb3259b@161.97.82.203:26256,392a7ec2683e288866c353b7a8ac9ecc4e7b4bfc@142.165.207.19:16656,b9b7e3d11ceffcd40261d3ae062307628817e1ff@212.8.240.13:2366,f7edad3ff5a85d039e7de12067c63064c5b42d63@46.4.121.72:11656,d9a458c840a46aa284ff9b3f1fc1df3b1cc5f386@51.195.234.250:26656,7b21198feaf0882f09fcbb24060961f434d158a3@35.242.163.107:26656,ae9f56518c60db2f79fb105c5b935febeb0226f0@198.244.203.194:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$PEERS'"|' $HOME/.quicksilverd/config/config.toml
```
