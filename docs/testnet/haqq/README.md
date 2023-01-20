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

**live-peers** (31)
```bash
peers="ed145a35b436878c1f1c10634bd18600f3696e17@95.217.181.142:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,56158e0f2acf850114e82644afceb565a73b08cc@185.144.99.95:26656,aed7038b96314fcb741168869c66029e6c6a58ef@34.90.39.222:26656,6771e65c1b30cc514faf5943320fdda480fe9124@95.216.39.183:26656,23ff658b56fbb8bc73372973a34733ff5d79b435@142.132.202.50:11604,32a8eec046b95e8646ff0810b4596dc7083a0beb@65.108.145.131:26656,125063c422e09faf45b849dd73dea61f624db891@65.109.53.60:26656,b9e8ec4eeb359e1b3cf5675563e72787b9d40adf@95.217.132.146:26656,3df5a68b919177179c6dcb0b9c9354fd6bbba1c8@65.109.92.240:20116,51e4544568cf880451bfffc292de88adc472f0e0@34.147.126.38:26656,ff6df373bf7bce436d488d2d8f5f5b283c6431d4@51.79.100.160:26656,90b40d2b773090b82aa7788c2d1937e4fd6d2dc0@65.108.231.124:19656,59af99085c961a6a5c8dc4bc8b3abffda16ddccb@135.181.38.62:26656,927a323649e7dd8d4c75da6e5edaee439652b46f@65.109.92.241:20116,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,24e894d4d8a18276acf6051cccf369a1ce69842d@65.108.151.105:26656,47a269c3e30f70d8234a2afd8e9055e74129fde0@65.108.129.29:36656,0833039f717227ccd156d156ea772746b8ac6d71@146.19.24.139:26656,ce0942b9676206400a68ce8fcdb1b1bb76f88226@155.133.27.197:36656,f57fae1bdea281392b563a58978a2d8c0a37725f@95.217.233.234:26656,6237a5c1f154e0e41738f038e204c0c60d7ad8e0@65.108.250.241:56656,1c5a4624a7f1a71e240ae2df82e97d5e9f46ff5c@88.99.214.188:60956,62d44513c7fd5aafa65773e5c015ca032f8eea4a@213.239.213.179:26656,0629018cef2e53288757381ffdc0b84cbb5931cc@95.216.1.249:26656,ee4db669ed2ff87cb2a47f848fa061517eb47737@161.97.151.46:26656,2fdcd211d7457390cc7de84dc5b87750f1ece442@121.4.161.226:35656,7f2828e3910a4b165a65e5bfb2465c1e809bad3b@65.108.48.182:26656,6fad54232f11a0306bd0d942c2ec5f9ba0ae2f1a@34.91.54.209:26656,00b1befaceba6b0178d2b6076ae0968adf4bd7b5@65.108.67.152:26656,9444cf6e8cc3e452f8006acce0283d87ee663b7a@185.163.125.253:35656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.haqqd/config/config.toml
```
