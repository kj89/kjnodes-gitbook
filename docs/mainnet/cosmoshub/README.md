# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/cosmoshub.png" alt=""><figcaption></figcaption></figure>

The Cosmos Hub is the blockchain protocol underlying an  increasingly large number of blockchains built on the  Cosmos Network, allowing them to communicate with each other.

**Chain ID**: cosmoshub-4 | **Latest Version Tag**: v9.0.0 | **Wasm**: OFF

[Website](https://hub.cosmos.network) | [Discord](https://discord.gg/cosmosnetwork) | [Twitter](https://twitter.com/cosmoshub)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/cosmoshub](https://explorer.kjnodes.com/cosmoshub)

## Public endpoints

* api: [https://cosmoshub.api.kjnodes.com](https://cosmoshub.api.kjnodes.com)
* rpc: [https://cosmoshub.rpc.kjnodes.com](https://cosmoshub.rpc.kjnodes.com)
* grpc: cosmoshub.grpc.kjnodes.com:13490

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@cosmoshub.rpc.kjnodes.com:13456
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@cosmoshub.rpc.kjnodes.com:13459
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/cosmoshub/addrbook.json > $HOME/.gaia/config/addrbook.json
```

**live-peers** (30)
```bash
peers="e726816f42831689eab9378d5d577f1d06d25716@23.88.22.1:26656,2286eeee09fcf37e768dfffc0db8c821b9231b7b@204.16.244.78:26656,51c49b57b371e3645de715e0034236a8bd61965e@35.221.229.109:26656,1b5a5b6518d3cb30a0d49cbd74a45dd4cbab130d@18.138.176.63:26656,c14d39422b5d70d9084d19d286c7427c0762cdfc@162.55.92.114:2010,81062b9a8807a1229543b84bae2898c50a1b1dfc@52.211.169.132:26656,9e14c8c48776a789f7029e88c260b2a6cbbf1417@35.212.85.141:26656,53b3651680ec3482d736808cbb3035940107f8ab@82.100.58.119:26656,1da54d20c7339713f1d6d28dd2117087dd33d0ca@5.9.59.145:26656,1279eae188599463661c3e2b9ab492615a6d7079@65.108.235.32:2010,9edd51012df3a09395a48eb68a84723d6308e08c@35.212.116.100:26656,b6b9bc1a0c18d12be759111bb3a0d9a8958120c7@57.128.20.184:26656,32bdba6ced12cdf2e534566e6c3d66ee2f7ef494@84.244.95.229:26656,e0ab6c5cc86959853f499236b8297344802ac5f4@5.161.139.201:26656,0eeb20e044d632b279e67f2fe91f50e4fceab1fd@159.223.223.84:26656,7abab0475a506ed3b9ab2ad40948bfe53b797e13@128.199.128.15:26090,1cce99042f884d669e7287e3e362bff8e385c63e@46.4.79.183:26726,07da4ffc5f6ed24960503ad046811f879e7f1823@44.214.37.79:26656,1733aef88702bd8326bea0e1dc403d3dbb6f5d8a@158.247.202.33:26656,6ecca845883e9273062ee515d2657080e6539d9e@65.109.32.148:26726,1de09530f959492df3fbb33cdd43895fc0dc17bd@34.249.39.245:26656,ca5011c44fd74d95e7fca487c69e301df195750c@65.108.122.246:26726,61afb0f37c02031f285f6b27ead2a3e7a97cc28a@35.212.34.104:26656,2532ad5b2f93fd521e97dbc3562db711df4bd763@65.109.88.70:26656,ee767901f4a7eaf44603ef0a5b6e5edac118ba1e@74.118.136.149:26656,9a9f789447f8c42b20ab8bbf847b4720672af82d@13.42.29.198:26656,2a821a6107e805cb990e7b416d224d1928a19fba@18.177.1.230:26656,241b17dba97a2ed3c3747d12781fb86c9706e2d4@89.58.27.86:26656,36515aac2a928e227e7dc793a548b35b54bec974@45.63.82.80:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:34656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gaia/config/config.toml
```
