# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/cosmoshub.png" width="150" alt=""><figcaption></figcaption></figure>

The Cosmos Hub is the blockchain protocol underlying an  increasingly large number of blockchains built on the  Cosmos Network, allowing them to communicate with each other.

**Chain ID**: cosmoshub-4 | **Latest Version Tag**: v9.0.0 | **Wasm**: OFF

[Website](https://hub.cosmos.network) | [Discord](https://discord.gg/cosmosnetwork) | [Twitter](https://twitter.com/cosmoshub)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/cosmoshub](https://explorer.kjnodes.com/cosmoshub)

## Public endpoints

* api: [https://cosmoshub.api.kjnodes.com](https://cosmoshub.api.kjnodes.com)
* rpc: [https://cosmoshub.rpc.kjnodes.com](https://cosmoshub.rpc.kjnodes.com)
* grpc: cosmoshub.grpc.kjnodes.com:34090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@cosmoshub.rpc.kjnodes.com:34656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@cosmoshub.rpc.kjnodes.com:34659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/cosmoshub/addrbook.json > $HOME/.gaia/config/addrbook.json
```

**live-peers** (30)
```bash
peers="c7a1d95db766b57bbea36ad1db1fc3cb41857fc8@86.111.48.38:26656,e829d4764a5cecc44b3414777853b34407b36601@185.16.39.179:26656,7abab0475a506ed3b9ab2ad40948bfe53b797e13@128.199.128.15:26090,e2b3cba06a28ff811e72f23d0e025c9354ed680d@35.206.163.4:26656,1cce99042f884d669e7287e3e362bff8e385c63e@46.4.79.183:26726,2286eeee09fcf37e768dfffc0db8c821b9231b7b@204.16.244.78:26656,c14d39422b5d70d9084d19d286c7427c0762cdfc@162.55.92.114:2010,81062b9a8807a1229543b84bae2898c50a1b1dfc@52.211.169.132:26656,61912dd14eb4e0c4588977491426b77fd7b0dcfc@141.95.72.172:26656,e0ab6c5cc86959853f499236b8297344802ac5f4@5.161.139.201:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:34656,1da54d20c7339713f1d6d28dd2117087dd33d0ca@5.9.59.145:26656,f5f8b96406a165d486be243723bfa7291db1cf62@35.230.170.155:26656,213857e741833d17275ea559bb2d0342398cec99@35.245.206.45:26656,ca5011c44fd74d95e7fca487c69e301df195750c@65.108.122.246:26726,971ed177b284db42108187867cb8694df48ac742@95.217.205.41:26656,4ddba29a7dfa740a4edeb5c620c963f67f951e1d@5.9.72.212:2000,0255a6594d169ea042a3a3694f279daf2eb7ab4a@103.126.158.30:26656,c940e11c1072dad06da3b1b48ca92966bb37e93a@74.96.207.58:28721,8a7a917fce1e71d66c86b765c1ba61f3d5266a07@54.74.25.142:26656,67685d93f2256caa7a2d53e3a104f9e437c3d247@95.216.114.244:26656,0eeb20e044d632b279e67f2fe91f50e4fceab1fd@159.223.223.84:26656,32bdba6ced12cdf2e534566e6c3d66ee2f7ef494@84.244.95.229:26656,b858ca4f3fed2c36b949cf67188b126e2542a39a@135.181.215.115:26726,4c46d32cbc4777c59a91a53fdadf8a3fa362036e@116.202.10.68:26656,3da88430414ec9084c8983fe4d462cce655ff1f3@51.222.245.114:26656,6ecca845883e9273062ee515d2657080e6539d9e@65.109.32.148:26726,5b143d463427d9ad0b621f97c0b8933643e293da@35.212.90.144:26656,8698cb819c9a4503fe2c71055f1380d08edc5adf@204.16.244.116:26656,fe21dd474640247888fc7c4dce82da8da08a8bfd@135.181.113.227:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gaia/config/config.toml
```
