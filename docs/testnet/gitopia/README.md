# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/gitopia.png" width="150" alt=""><figcaption></figcaption></figure>

Gitopia is the next-generation Code Collaboration Platform fuelled by  a decentralized network and interactive token economy. It is designed  to optimize the open-source software development process through  collaboration, transparency, and incentivization.

**Chain ID**: gitopia-janus-testnet-2 | **Latest Version Tag**: v1.2.0 | **Wasm**: OFF

[Website](https://gitopia.com/) | [Discord](https://discord.gg/hFTXCGNYDZ) | [Twitter](https://twitter.com/gitopiaDAO)


## Public endpoints

* rpc: [https://gitopia-testnet.rpc.kjnodes.com](https://gitopia-testnet.rpc.kjnodes.com)
* api: [https://gitopia-testnet.api.kjnodes.com](https://gitopia-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@gitopia-testnet.rpc.kjnodes.com:41656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@gitopia-testnet.rpc.kjnodes.com:41659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/gitopia-testnet/addrbook.json > $HOME/.gitopia/config/addrbook.json
```

**live-peers** (35)
```
peers="37677351ed74a5ced46a99217d19e30d5bcacc1d@5.75.147.138:26656,2f58a44c9ce9dcdf81e2eaed7cd808ebefe222a7@38.242.243.111:26656,32254e5e11c49d8802f4c5bbd2c682eebd72ea33@80.241.220.28:60956,bd4375ea3398dd700195dbae3218f95e512908ee@194.163.172.251:41656,5ffdc1788f68df5e8163d9bd0d71a4c4d3dec2e9@81.0.220.21:26656,31099d763305ead833b84c28b142ecbfd3628a64@85.190.246.250:41656,e88708f6bda2af195f0ec48b9868e588ead964fb@144.91.82.239:26656,458a98d6293064bdf3d6f86e0e2aa87bbb450f07@75.119.144.48:656,b30d41820868f19784589dce150f07e3bdce8ea2@86.48.0.95:26656,95fbdc6d62be17db6688222b15b57d3e795ed07a@167.86.84.102:656,b44d4fd0799d2c06fbec0257b376c0520bdb226a@185.250.37.147:41656,481189b7e246f6c824a969482446c49abbfe76b8@161.97.172.147:26656,c40217eafa32447028bfe62f3c4dd20c14cef94e@173.249.57.208:656,c820e754c56b5455d64ab7685730c44a936d0833@154.38.165.129:26656,938ac1e4262cb2341bac323156fc3637f1b9c472@84.46.240.25:41656,85236d0c81cad2ce71c59b7aa7ab191bce545bff@89.117.50.45:656,016b0e565abd496b9473b87ac41339251005d12e@194.163.167.163:41656,e79532749fb5dd95366f4568a7b2430d0e316fb5@84.46.255.163:26656,6d36c85a0fc1d737906f47af2e090734e0f6d4a3@86.48.3.99:26656,0eb70bf5e2403694109f9bba184570074c2dfdd5@38.242.235.255:26656,ea53a3f77fe373f47be4e77fd5f9ff526dfaec33@51.79.143.46:41656,5171aad5f862d474b36fc8049be3339068c96cc9@165.232.151.144:26656,ee812a11525cf7e2de4bd63e66aed8b8de337902@38.242.235.199:41656,b6651c7b043ef4bdccd7906b0f06de2bbdfe8a60@193.46.243.75:26656,44a66336b029ba931165da3580cc6322af90339d@38.242.207.87:26656,19fb417249992ae8def277fb753656da318fe250@38.242.133.239:41656,f4d2fd4a8f21c40559b1c903aaae0b0b1c937dc4@194.61.28.39:41656,aec8ea46d0e5d0688b58df8a47c6934959fe981f@65.109.90.33:11356,63381c5528ed8ca93f9ba31008a9630d21b29a97@142.132.152.46:46656,5c2c2b27e1824097d4f5dc7a581a8d615923e76f@185.252.235.110:41656,a8591524ebded3132f423771c0d91b77bdffad44@82.208.22.16:26656,38f4e436b28b05850fa9b67cadf0700123cec094@45.10.154.166:26656,4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,eb34bba81406640084995e7a3f732187509ae2e8@164.92.113.87:41656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
