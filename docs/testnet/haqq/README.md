# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/haqq.png" width="150" alt=""><figcaption></figcaption></figure>

Haqq is the blockchain network that issues Islamic Coin,  its native cryptocurrency. Haqq is fast, trusted and  compatible with thousands of applications around the world.

**Chain ID**: haqq_54211-3 | **Latest Version Tag**: v1.3.1 | **Wasm**: OFF

[Website](https://islamiccoin.net) | [Discord](https://discord.gg/hU9MHG5kZq) | [Twitter](https://twitter.com/Islamic_Coin)




## Chain explorer
[https://explorer.kjnodes.com/haqq-testnet](https://explorer.kjnodes.com/haqq-testnet)

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

**live-peers** (38)
```bash
peers="32a8eec046b95e8646ff0810b4596dc7083a0beb@65.108.145.131:26656,f50b6abb555c0d420834860d9a8f499801bb3ae8@135.181.62.222:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,56158e0f2acf850114e82644afceb565a73b08cc@185.144.99.95:26656,6771e65c1b30cc514faf5943320fdda480fe9124@95.216.39.183:26656,3df5a68b919177179c6dcb0b9c9354fd6bbba1c8@65.109.92.240:20116,48a2a7762a579d25bca95b0a3548b714238dd60b@213.239.216.252:20656,0833039f717227ccd156d156ea772746b8ac6d71@146.19.24.139:26656,ee4db669ed2ff87cb2a47f848fa061517eb47737@161.97.151.46:26656,23ff658b56fbb8bc73372973a34733ff5d79b435@142.132.202.50:11604,927a323649e7dd8d4c75da6e5edaee439652b46f@65.109.92.241:20116,62bf004201a90ce00df6f69390378c3d90f6dd7e@45.83.173.19:26656,51e4544568cf880451bfffc292de88adc472f0e0@34.147.126.38:26656,001eb7a3a03dc11539541737262c4ddc84dec283@91.195.101.98:26656,59af99085c961a6a5c8dc4bc8b3abffda16ddccb@135.181.38.62:26656,b72f2156db8c87e679dc853730746ff40038120c@213.239.215.77:26656,78e3ef8adf819b479acc13a2f92ab5c0fa350aeb@66.45.231.30:11464,b60e128a16202a9913961f77e1d2160e0aae87d3@178.170.42.198:36656,ba56c564a5430632e59e2b08fc348735bc56b32f@154.12.232.140:26656,ed145a35b436878c1f1c10634bd18600f3696e17@95.217.181.142:26656,24e894d4d8a18276acf6051cccf369a1ce69842d@65.108.151.105:26656,97fbe24743895fe58ee7fb6a60a3c7826494f446@65.109.58.237:26656,6b0115c6b866544b201342b1d63374451bdc8d4e@31.134.187.134:35656,90b40d2b773090b82aa7788c2d1937e4fd6d2dc0@65.108.231.124:19656,47a269c3e30f70d8234a2afd8e9055e74129fde0@65.108.129.29:36656,43dc2d5ab6fa30cb10959717d26f31bc45b56fdd@149.102.133.67:35656,a6150d39e4725d28a56f41ebf3c6d457c54bd2f1@34.138.250.4:26656,d7ac44bf8f8d760c3df1a8695145021f35feb985@34.88.220.124:26656,0629018cef2e53288757381ffdc0b84cbb5931cc@95.216.1.249:26656,7094f2c1ee04801b76159bd614eb5947ffc8c5d9@109.71.177.3:35656,9f91d1845f0bd759ff6b83ba5e0f6f6650f57fa2@149.102.132.135:35656,6ce864d853904ebef9400528f129d8fefa6f1827@91.211.251.232:36656,8874e948e646cfb43ae1c5bdb69c1badf97285fc@149.102.128.160:26656,99a8389c84625503c2b8d734dfd78035d28e4f15@65.109.30.117:26656,1a68f19b58e0c4e99c907a3c43923641a1595c88@149.102.133.29:35656,f57fae1bdea281392b563a58978a2d8c0a37725f@95.217.233.234:26656,a884387139109784cad9193652b82ef20a85d713@38.242.159.148:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.haqqd/config/config.toml
```
