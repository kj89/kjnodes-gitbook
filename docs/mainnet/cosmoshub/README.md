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
peers="25d3ec5a00235fe95d7a87bab54f03b6ac1962ba@34.78.95.235:26656,ee767901f4a7eaf44603ef0a5b6e5edac118ba1e@74.118.136.149:26656,d484b416598b98d3cd7f4dfb6faa30d75ee9d545@188.214.129.233:26656,1da54d20c7339713f1d6d28dd2117087dd33d0ca@5.9.59.145:26656,32bdba6ced12cdf2e534566e6c3d66ee2f7ef494@84.244.95.229:26656,971ed177b284db42108187867cb8694df48ac742@95.217.205.41:26656,9d048653fa4d98e6c0760ed0c54ad2d257ba46df@65.108.137.34:26656,9edd51012df3a09395a48eb68a84723d6308e08c@35.212.116.100:26656,e2b3cba06a28ff811e72f23d0e025c9354ed680d@35.206.163.4:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:34656,b6b9bc1a0c18d12be759111bb3a0d9a8958120c7@57.128.20.184:26656,b858ca4f3fed2c36b949cf67188b126e2542a39a@135.181.215.115:26726,3da88430414ec9084c8983fe4d462cce655ff1f3@51.222.245.114:26656,0eeb20e044d632b279e67f2fe91f50e4fceab1fd@159.223.223.84:26656,c940e11c1072dad06da3b1b48ca92966bb37e93a@74.96.207.58:28721,36515aac2a928e227e7dc793a548b35b54bec974@45.63.82.80:26656,6ecca845883e9273062ee515d2657080e6539d9e@65.109.32.148:26726,d53ecee926a66a4a6b1858004f5f22f77faca036@3.69.52.20:26656,ca5011c44fd74d95e7fca487c69e301df195750c@65.108.122.246:26726,fe21dd474640247888fc7c4dce82da8da08a8bfd@135.181.113.227:26656,d25bd1bea59f3a96bcb98b6da6f5cf874ac59179@54.236.120.119:26656,1279eae188599463661c3e2b9ab492615a6d7079@65.108.235.32:2010,e829d4764a5cecc44b3414777853b34407b36601@185.16.39.179:26656,0255a6594d169ea042a3a3694f279daf2eb7ab4a@103.126.158.30:26656,dea13e7232642331360d4387b0ab106b014092d4@116.202.236.59:26656,cfd785a4224c7940e9a10f6c1ab24c343e923bec@164.68.107.188:26656,64a0909aa38311baaba615c6299a4ca9d27fd7ef@44.209.21.229:26656,27ad834c62dbefc5beb74be7575515927bd07c58@193.176.85.151:26656,1cce99042f884d669e7287e3e362bff8e385c63e@46.4.79.183:26726,cd372322e563832871672be23d8303508d4385a3@139.59.8.48:26090"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gaia/config/config.toml
```
