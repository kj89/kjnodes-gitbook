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

**live-peers** (30)
```bash
peers="afa529ce3a5f2effcb21b2ee1bb7fe677476ed76@167.235.7.34:36656,96cd4df06277f3353fa2da1f73d8e21663183c3f@91.107.192.98:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,927a323649e7dd8d4c75da6e5edaee439652b46f@65.109.92.241:20116,230d299006a432b0f44534ca8a19c8c876c0ccb3@85.10.193.246:26656,62bf004201a90ce00df6f69390378c3d90f6dd7e@45.83.173.19:26656,ce33c379191a7f741165d9538fc4d3d8773381ac@69.197.30.3:24416,23ff658b56fbb8bc73372973a34733ff5d79b435@142.132.202.50:11604,3df5a68b919177179c6dcb0b9c9354fd6bbba1c8@65.109.92.240:20116,29731457774b61da8186b9c764e8f7c1e2465e3e@142.93.36.176:26656,442d3bacb350437b8d9f0f1431e0519b81094100@135.181.62.222:26656,16f40215d018c7d657fef0bb5ce2950251d525d2@148.251.51.144:36656,bc777df96c83c0433561c88c541dbbc520928f6c@195.3.221.239:26656,6de69146d5ebbc0b8cd9ecdf4b33edb57bf9b559@185.187.170.133:26656,ffc8b0dbe8eea3083320cdc014cc6ce8f60e5096@23.88.74.54:35656,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,78e3ef8adf819b479acc13a2f92ab5c0fa350aeb@66.45.231.30:11464,331ca63236ba05842d561e22c0bcc8582efa60a1@209.126.80.192:26656,23a1176c9911eac442d6d1bf15f92eeabb3981d5@45.83.173.18:26656,c1daefce01efd7ab1c10bd503d386d08cf03c573@78.47.51.242:26656,a6150d39e4725d28a56f41ebf3c6d457c54bd2f1@34.138.250.4:26656,d7ac44bf8f8d760c3df1a8695145021f35feb985@34.88.220.124:26656,a884387139109784cad9193652b82ef20a85d713@38.242.159.148:26656,b9e8ec4eeb359e1b3cf5675563e72787b9d40adf@95.217.132.146:26656,99a8389c84625503c2b8d734dfd78035d28e4f15@65.109.30.117:26656,8865bf7e0575d3033b54d41854ed117ee40983bd@3.125.7.6:26656,62a8610cc2325cbdf25099b973ae488a05f7d417@65.108.206.57:13656,f54d4de6d4ae81ec8a2315b54247872b315f198d@65.109.57.9:26656,6ce864d853904ebef9400528f129d8fefa6f1827@91.211.251.232:36656,3f5110515b76596e05a447fd50e4727eaad00124@188.34.201.77:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.haqqd/config/config.toml
```
