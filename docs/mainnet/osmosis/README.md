# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/osmosis.png" width="150" alt=""><figcaption></figcaption></figure>

Osmosis is a DEX protocol, which means it uses smart contracts  to determine the price of digital assets, to produce liquidity  via a peer-to-peer (P2P) methodology, and to exact trades between users

**Chain ID**: osmosis-1 | **Latest Version Tag**: v15.0.0 | **Wasm**: ON

[Website](https://osmosis.zone) | [Discord](https://discord.gg/osmosis) | [Twitter](https://twitter.com/osmosiszone)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/osmosis](https://explorer.kjnodes.com/osmosis)

## Public endpoints

* api: [https://osmosis.api.kjnodes.com](https://osmosis.api.kjnodes.com)
* rpc: [https://osmosis.rpc.kjnodes.com](https://osmosis.rpc.kjnodes.com)
* grpc: osmosis.grpc.kjnodes.com:29090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@osmosis.rpc.kjnodes.com:29656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@osmosis.rpc.kjnodes.com:29659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/osmosis/addrbook.json > $HOME/.osmosisd/config/addrbook.json
```

**live-peers** (30)
```bash
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,4e38d3caa1554d7f46a2654fa9997554c13f61f2@95.216.96.61:26656,2f4c0337b2522034a614a5cb2c61a891fe753c03@5.9.81.187:29656,2cb8dd6195c65458e3c18505bb70ce2ff624f85c@89.58.61.223:2000,94e69330d6f4cfe221cdd2ce49ee141e53e5f200@23.106.120.6:26656,b69e57cd6f796ac5d6efb1a834163365c37cbfa8@78.46.69.29:26656,406f64a8d601e34d7311fd61ec87b0c7028bd230@138.201.23.39:46656,22c0c06ee183b47d75f8d8ec6d6c63dca90c90e5@54.156.184.104:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@169.155.169.186:26656,c0c2c6ff9e456dc31c7f697c81168267dbb49339@34.83.112.45:26656,63b4a45bb2276fe141e69ce83750a2c53f1ceeda@198.244.202.196:26656,f9a920a61ee994b12b77178dd5f1fc1ed39b7cd2@142.132.255.49:26656,88fa3de90d06422b409ce6beb2367b94b2a1759e@51.79.17.73:26656,4cccbb26639559c39f44758d246c5ed928f7717f@176.9.19.66:26656,c257db7b3a7f61688c6452d1e9dcfb3034e54fe8@143.198.98.144:26656,13d17adf418ceab5528096dcacf130830fee2b86@35.215.50.201:26656,3d311ac374e6953e97ee07c74a76f399394c3025@173.215.85.171:20000,3226b67b2bb9da41b633392a785e87e8f6749939@162.55.245.149:12000,8a0caf4581f135b1468408ec398d94573da02e8c@198.244.202.140:26656,65f51ebf46256d829ae5903e9faf31dae35bdf46@65.109.64.245:26656,913e9db0332df1152e5afe032ab81bdb65e3f91c@110.11.23.44:26656,7f36123a395e902deaecf63bdaf5656bbb209623@15.204.52.75:26656,75bae7b2af60155b6687ca3e5f92010d35cb0c12@54.164.100.216:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@178.211.139.77:26716,91adf02a763df16ee33674c0d404377c63131efa@3.18.21.110:26656,2d06b9ae6c8c359fb4ab84f7b88a0429d2095a6b@65.109.111.235:26656,23d67702fc76a2f3b3f3b74876727934843cff94@195.14.6.2:26656,3197daa0ee5245b17a546be032ff0f6814e1d1db@148.251.191.239:26656,34340a9151d4a97a850d2cd64d8778279faf3f96@194.163.181.100:26656,ef573bd8b519f9572798444f6c229ab0a3204bb8@5.9.94.24:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
