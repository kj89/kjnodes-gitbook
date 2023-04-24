# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/haqq.png" width="150" alt=""><figcaption></figcaption></figure>

Haqq is the blockchain network that issues Islamic Coin,  its native cryptocurrency. Haqq is fast, trusted and  compatible with thousands of applications around the world.

**Chain ID**: haqq_54211-3 | **Latest Version Tag**: v1.3.1 | **Wasm**: OFF

[Website](https://islamiccoin.net) | [Discord](https://discord.gg/hU9MHG5kZq) | [Twitter](https://twitter.com/Islamic_Coin)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/haqq-testnet](https://explorer.kjnodes.com/haqq-testnet)

## Public endpoints

* api: [https://haqq-testnet.api.kjnodes.com](https://haqq-testnet.api.kjnodes.com)
* rpc: [https://haqq-testnet.rpc.kjnodes.com](https://haqq-testnet.rpc.kjnodes.com)
* grpc: haqq-testnet.grpc.kjnodes.com:35090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@haqq-testnet.rpc.kjnodes.com:35656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@haqq-testnet.rpc.kjnodes.com:35659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/haqq-testnet/addrbook.json > $HOME/.haqqd/config/addrbook.json
```

**live-peers** (29)
```bash
peers="442d3bacb350437b8d9f0f1431e0519b81094100@135.181.62.222:26656,c1daefce01efd7ab1c10bd503d386d08cf03c573@78.47.51.242:26656,230d299006a432b0f44534ca8a19c8c876c0ccb3@85.10.193.246:26656,927a323649e7dd8d4c75da6e5edaee439652b46f@65.109.92.241:20116,3df5a68b919177179c6dcb0b9c9354fd6bbba1c8@65.109.92.240:20116,6b5059a1d17f2e436f55bdbe9fa3280f27483fb3@162.55.235.69:36656,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,32a8eec046b95e8646ff0810b4596dc7083a0beb@65.108.145.131:26656,589f76a7932cf6d4ecf601a11ccc0a721b9a4ee4@65.109.85.170:29656,9eb507f9365313dbe7f426050fec9648298f58ee@109.205.183.51:26656,24e894d4d8a18276acf6051cccf369a1ce69842d@65.108.151.105:26656,62bf004201a90ce00df6f69390378c3d90f6dd7e@45.83.173.19:26656,23ff658b56fbb8bc73372973a34733ff5d79b435@142.132.202.50:11604,d7ac44bf8f8d760c3df1a8695145021f35feb985@34.88.220.124:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,088a622ef2539ba07d83af284a61f134a99f063b@95.217.35.186:26656,23a1176c9911eac442d6d1bf15f92eeabb3981d5@45.83.173.18:26656,16f40215d018c7d657fef0bb5ce2950251d525d2@148.251.51.144:36656,ed145a35b436878c1f1c10634bd18600f3696e17@95.217.181.142:26656,f54d4de6d4ae81ec8a2315b54247872b315f198d@65.109.57.9:26656,5c11c697aaf2dabf96e3eb7e7e621c200bd309ee@65.21.225.58:26656,a6150d39e4725d28a56f41ebf3c6d457c54bd2f1@34.138.250.4:26656,78e3ef8adf819b479acc13a2f92ab5c0fa350aeb@66.45.231.30:11464,a884387139109784cad9193652b82ef20a85d713@38.242.159.148:26656,6eb774812df88238e7a1febeff940d43f56c3c7c@213.239.207.175:26641,93ae3fa625f55b98225b870e4fd4052ad8a97b97@109.123.252.231:26656,acba49be707c31a831a3bca9d9d9f7defcc0bd21@142.132.148.174:26656,62a8610cc2325cbdf25099b973ae488a05f7d417@65.108.206.57:13656,f57fae1bdea281392b563a58978a2d8c0a37725f@95.217.233.234:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.haqqd/config/config.toml
```
