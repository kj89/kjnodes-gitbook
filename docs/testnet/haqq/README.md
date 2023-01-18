# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/haqq.png" width="150" alt=""><figcaption></figcaption></figure>

Haqq is the blockchain network that issues Islamic Coin,  its native cryptocurrency. Haqq is fast, trusted and  compatible with thousands of applications around the world.

**Chain ID**: haqq_54211-3 | **Latest Version Tag**: v1.3.0 | **Wasm**: OFF

[Website](https://islamiccoin.net) | [Discord](https://discord.gg/hU9MHG5kZq) | [Twitter](https://twitter.com/Islamic_Coin)


## Public endpoints

* api: [https://haqq-testnet.api.kjnodes.com](https://haqq-testnet.api.kjnodes.com)
* rpc: [https://haqq-testnet.rpc.kjnodes.com](https://haqq-testnet.rpc.kjnodes.com)
* grpc: [https://haqq-testnet.grpc.kjnodes.com](https://haqq-testnet.grpc.kjnodes.com)

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

**live-peers** (24)
```bash
peers="927a323649e7dd8d4c75da6e5edaee439652b46f@65.109.92.241:20116,ba56c564a5430632e59e2b08fc348735bc56b32f@154.12.232.140:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,56158e0f2acf850114e82644afceb565a73b08cc@185.144.99.95:26656,23ff658b56fbb8bc73372973a34733ff5d79b435@142.132.202.50:11604,125063c422e09faf45b849dd73dea61f624db891@65.109.53.60:26656,6771e65c1b30cc514faf5943320fdda480fe9124@95.216.39.183:26656,59af99085c961a6a5c8dc4bc8b3abffda16ddccb@135.181.38.62:26656,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,3df5a68b919177179c6dcb0b9c9354fd6bbba1c8@65.109.92.240:20116,0629018cef2e53288757381ffdc0b84cbb5931cc@95.216.1.249:26656,b9e8ec4eeb359e1b3cf5675563e72787b9d40adf@95.217.132.146:26656,90b40d2b773090b82aa7788c2d1937e4fd6d2dc0@65.108.231.124:19656,0833039f717227ccd156d156ea772746b8ac6d71@146.19.24.139:26656,32a8eec046b95e8646ff0810b4596dc7083a0beb@65.108.145.131:26656,1fefb6b75431482502e125a290deba1e7e539d4e@135.181.148.11:26656,54e81994c61bbb6c414f8ab0a606a7edda138a3b@95.216.154.100:26656,51e4544568cf880451bfffc292de88adc472f0e0@34.147.126.38:26656,7f2828e3910a4b165a65e5bfb2465c1e809bad3b@65.108.48.182:26656,00b1befaceba6b0178d2b6076ae0968adf4bd7b5@65.108.67.152:26656,6fad54232f11a0306bd0d942c2ec5f9ba0ae2f1a@34.91.54.209:26656,62d44513c7fd5aafa65773e5c015ca032f8eea4a@213.239.213.179:26656,24e894d4d8a18276acf6051cccf369a1ce69842d@65.108.151.105:26656,d59dc597f0d41bcbc7ff53374686affb143726c2@51.195.203.103:35656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.haqqd/config/config.toml
```
