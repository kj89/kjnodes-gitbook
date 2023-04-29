# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/uptick.png" alt=""><figcaption></figcaption></figure>

Uptick Network is building business-grade infrastructure and  ecosystems for non-fungible tokens (NFTs). The platform is  designed with a focus on multi-chain and cross-chain interoperability,  and includes three key components: the NFT infrastructure, an NFT  marketplace, and NFT ecosystem applications.

**Chain ID**: uptick_7000-2 | **Latest Version Tag**: v0.2.6 | **Wasm**: OFF

[Website](https://uptick.network) | [Discord](https://discord.gg/UzeHS7fu5H) | [Twitter](https://twitter.com/uptickproject)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/uptick-testnet](https://explorer.kjnodes.com/uptick-testnet)

## Public endpoints

* api: [https://uptick-testnet.api.kjnodes.com](https://uptick-testnet.api.kjnodes.com)
* rpc: [https://uptick-testnet.rpc.kjnodes.com](https://uptick-testnet.rpc.kjnodes.com)
* grpc: uptick-testnet.grpc.kjnodes.com:15090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@uptick-testnet.rpc.kjnodes.com:15656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@uptick-testnet.rpc.kjnodes.com:15659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/uptick-testnet/addrbook.json > $HOME/.uptickd/config/addrbook.json
```

**live-peers** (28)
```bash
peers="b9d3fe835ded0b93c39befad43fb3c4964ae740f@91.195.101.100:26656,9de4c96ffa9540286b5251b50dd373ac46da3cdd@178.63.52.213:11656,9b7b2fb9d1416f9feadf5a58b29de0bc150d974d@65.109.89.5:30656,1c66685cbf5c8dc0a739eb57c896d35eb2eed17c@65.109.50.106:28656,0148cb2bb6b646cb147b1651ad503fcf9abfc652@107.155.98.194:36656,b483acbcae7ccd1244f588144245e9d1124c3de5@88.99.56.200:26666,7831b5c5cc90fa95ea99a0cea5d1ad07dfcc7b9c@185.245.183.187:26656,af5262526a0800a29a0a7194e1488a9fa62d0005@195.3.223.208:26656,a818920590d15226a206ec4c73b1c5c20c56a435@65.21.134.202:26666,3edfe380f7eff0658582c158f2eecebae2e0fed7@213.239.213.179:26656,eb5a3112a64944e2bd701ff8aa99ab95209c6310@185.198.27.110:26656,174a57a0d4b914b5a9823a5f3f47ae4b06d9809e@65.108.206.118:60956,7849e4320385434b0828a3e0206a3b69767393f6@65.109.91.227:26656,1bb6d67af0dd1d452e294e9df430d07bccefe502@185.215.167.241:26656,e24bde7fe207160442fe6b93ee376a739def5757@51.222.248.153:26656,d8777278648d8fc93800692a8b96a7f104df4f9a@194.163.135.127:26656,0afb5ce897e69eec34fb32bf87f4a2f93f79e0b3@65.109.65.210:30656,2298edffe9306e4d9370233c1d29dab567829095@144.91.78.28:26656,878101ab9ad2402bfd700a3da58223778461c753@185.245.182.152:26656,7a4f1c0baa2ff31c02163fb658c4eb8d119193c7@95.214.52.173:18656,be823fc2f0e81ac3003ec20eba05bd963c0f3aac@95.217.4.62:26656,86f50af23369997882ca3988eabeba998b4f07cc@65.109.92.79:10656,52cdb51fe8692dea11de23b8c97c9d947a6eb1c2@51.222.44.116:10656,8eaa8bc68e79a3c9b2037f4f675985cdbb1657e4@65.109.136.251:26656,6a775f6034f64827a6220de07b1ad344284bbf51@194.163.155.84:46656,81e9fbb53928efafad7862722c16820ed7c0e5b7@65.21.225.207:10656,5739ae6fab71ec95fb3112f4d1ea2845782fa9f7@54.92.137.6:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.uptickd/config/config.toml
```
