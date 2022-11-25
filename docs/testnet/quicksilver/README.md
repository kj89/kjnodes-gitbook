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

**live-peers** (28)
```
peers="a854277e77b0ac095e53156266cdc39ad4b13b2f@142.132.205.94:15619,41f7d7004cace7bd1760a5f980a86123700c8f1d@185.146.148.116:26656,5844010472bac487748336616d450bc9f0cbc57c@65.108.72.175:29656,392a7ec2683e288866c353b7a8ac9ecc4e7b4bfc@142.165.207.19:16656,8ff8a186fe9cbc70d0f34891fa051f87e561a48b@158.160.0.93:26656,2096650d8586b858d3369205f3b46ac4c765bc8e@65.109.53.155:26656,0551eaa0db7097274410ee27a71672817e314b83@167.235.245.191:26656,cb6ae22e1e89d029c55f2cb400b0caa19cbe5523@137.184.162.34:26603,20b6b3f6c0927c14a2348f5e378b98cb8596fc06@34.105.195.160:26656,dc88be3a0075ce429a423237abe223a9528ce0df@65.108.204.119:31656,0a3ac40a7a4ce35978c4da97be2eb6974bc3c58b@185.252.233.217:46656,e0f0703e9ce343c46e0ec01b19216715e817b358@65.109.85.170:28656,7b21198feaf0882f09fcbb24060961f434d158a3@35.242.163.107:26656,433f85361545a434ad6b4202e2f373e4894ecf39@142.132.151.99:15619,c133c4c0c7034c8c345330f394984ad08092fc14@138.201.17.11:27656,5c6bfcfd42e8a4cf7960cf8b1860eed3de17196d@65.108.75.237:2010,7fe3007cba4de49584cbdad9489ffecfc9651c57@65.108.79.246:26673,f43bbd9bdceca5195a1b447adcc9108e4b960518@195.201.165.123:21026,bda5bc971df076b70b4447b842e634948516c5cb@65.108.105.48:14656,b02f304fa0f10090491f62bf12ed32bf73138d5c@148.72.153.85:11656,13564ca7ffcc8fa6bcc6d405c96fe8c724ec17da@88.99.213.25:11656,47a7fac621a79649519eadbb8deb92d33bb3259b@161.97.82.203:26256,03332cdbc3d354846a18992effbb8c20aa28f52a@65.21.133.125:28656,2caa7ddd45818914e96f540d2fc71784826bc660@161.97.155.94:26656,c4489720ba051c79f5bb16ae5d81341b0f248e19@54.194.109.230:26656,7d112277450f0a8ef1059e6b334c373a215726ea@23.88.0.170:15619,933bc9b7407db200892836ad24c91fcdb1e51c14@76.144.212.11:26656,f7edad3ff5a85d039e7de12067c63064c5b42d63@46.4.121.72:11656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.quicksilverd/config/config.toml
```
