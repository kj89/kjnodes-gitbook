# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/cosmoshub.png" alt=""><figcaption></figcaption></figure>

The Cosmos Hub is the blockchain protocol underlying an  increasingly large number of blockchains built on the  Cosmos Network, allowing them to communicate with each other.

**Chain ID**: cosmoshub-4 | **Latest Version Tag**: v9.1.0 | **Wasm**: OFF

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

**live-peers** (10)
```bash
peers="1f1bd2088351943c4a90036531bc027aa9860abc@134.65.192.166:26656,971ed177b284db42108187867cb8694df48ac742@95.217.205.41:26656,81062b9a8807a1229543b84bae2898c50a1b1dfc@52.211.169.132:26656,25d3ec5a00235fe95d7a87bab54f03b6ac1962ba@34.78.95.235:26656,7fbd001395634160be66bbcf08651fed5e0b9b64@162.19.18.137:7001,edaf53d23f324a6e3970dd39906d04ce3a1a1e31@135.181.54.227:26656,0eeb20e044d632b279e67f2fe91f50e4fceab1fd@159.223.223.84:26656,d32dfbb1a39d6ad97d24107a1b6c3d0018ca0fec@45.77.181.31:26656,b858ca4f3fed2c36b949cf67188b126e2542a39a@135.181.215.115:26726,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13456"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gaia/config/config.toml
```
