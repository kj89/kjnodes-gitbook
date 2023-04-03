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
peers="6a45e3655209dacddedf735a898ccfcae085abec@65.109.182.72:26656,61afb0f37c02031f285f6b27ead2a3e7a97cc28a@35.212.34.104:26656,1da54d20c7339713f1d6d28dd2117087dd33d0ca@5.9.59.145:26656,1733aef88702bd8326bea0e1dc403d3dbb6f5d8a@158.247.202.33:26656,e829d4764a5cecc44b3414777853b34407b36601@185.16.39.179:26656,b858ca4f3fed2c36b949cf67188b126e2542a39a@135.181.215.115:26726,1279eae188599463661c3e2b9ab492615a6d7079@65.108.235.32:2010,fe21dd474640247888fc7c4dce82da8da08a8bfd@135.181.113.227:26656,1cce99042f884d669e7287e3e362bff8e385c63e@46.4.79.183:26726,c940e11c1072dad06da3b1b48ca92966bb37e93a@74.96.207.58:28721,9e14c8c48776a789f7029e88c260b2a6cbbf1417@35.212.85.141:26656,d35f08a60aeb2729d07e92e778b4c6f83379092e@18.138.160.68:26656,9edd51012df3a09395a48eb68a84723d6308e08c@35.212.116.100:26656,3da88430414ec9084c8983fe4d462cce655ff1f3@51.222.245.114:26656,050aba124aadd089ad199b2e1d871ce03bf6ce4d@34.194.203.109:26656,971ed177b284db42108187867cb8694df48ac742@95.217.205.41:26656,9d048653fa4d98e6c0760ed0c54ad2d257ba46df@65.108.137.34:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:34656,7abab0475a506ed3b9ab2ad40948bfe53b797e13@128.199.128.15:26090,0eeb20e044d632b279e67f2fe91f50e4fceab1fd@159.223.223.84:26656,8dbc1e00c528ff2a160bfd7004024c17b237c19c@18.235.42.46:26656,9c116194f25fd0d146019f171ef0f49904dcc586@167.86.98.230:26656,36515aac2a928e227e7dc793a548b35b54bec974@45.63.82.80:26656,ca5011c44fd74d95e7fca487c69e301df195750c@65.108.122.246:26726,32bdba6ced12cdf2e534566e6c3d66ee2f7ef494@84.244.95.229:26656,8a210f1bcfc9015a7bc18dcc5add29c0dce3f2dc@95.217.127.25:26656,4ebf074e8b4a24438bd0bd503b62b4728dfb8eae@35.212.101.35:26656,e2b3cba06a28ff811e72f23d0e025c9354ed680d@35.206.163.4:26656,2e470eb2dfd65ffa34a9ae2d73646f82c6e594b7@65.108.10.36:26656,1997e68bf205bedeed0c4723786bf03464987dc1@77.87.108.21:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gaia/config/config.toml
```
